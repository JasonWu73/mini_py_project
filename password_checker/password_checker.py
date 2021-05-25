import hashlib
import sys

import requests


class PasswordChecker:

  def __init__(self):
    self.url = 'https://api.pwnedpasswords.com/range/'

  def check_pwned_password(self, password):
    hashed_password = self._generate_sha1_hash(password)
    first_5_hash_char, hash_tail = hashed_password[:5], hashed_password[5:]
    url_response = self._request_api_data(first_5_hash_char)
    response_text = url_response.text

    return self._get_password_leak_count(response_text, hash_tail)

  def _get_password_leak_count(self, response_text, password_tail):
    tail_count_tuple = (line.split(':') for line in response_text.splitlines())

    for tail, count in tail_count_tuple:
      if tail == password_tail:
        return int(count)

    return 0

  def _request_api_data(self, first_5_hash_char):
    url_response = requests.get(self.url + first_5_hash_char)
    if url_response.status_code != 200:
      raise RuntimeError(f'API 请求失败 [{url_response.status_code}]')
    return url_response

  def _generate_sha1_hash(self, string_need_to_sha1):
    return hashlib.sha1(string_need_to_sha1.encode('utf-8')).hexdigest().upper()


if __name__ == '__main__':
  passwords = sys.argv[1:]
  password_checker = PasswordChecker()

  for password in passwords:
    if len(password.strip()) > 0:
      pwned_count = password_checker.check_pwned_password(password)
      if pwned_count > 0:
        print(f'密码 {password} 已泄露 {pwned_count} 次，故不要再使用该密码了')
      else:
        print(f'密码 {password} 很安全，可以使用')
