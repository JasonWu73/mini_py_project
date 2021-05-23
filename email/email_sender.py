#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template


class EmailSender:

  def __init__(self):
    self.smtp_password = self._read_smtp_password()
    self.email = self._create_email()

  def send_email(self):
    with smtplib.SMTP(host='smtp.163.com') as smtp_server:
      smtp_server.ehlo()
      smtp_server.starttls()
      smtp_server.login('wuxianjiezh@163.com', self.smtp_password)
      smtp_server.send_message(self.email)
      print('邮件发送成功')

  def _read_smtp_password(self):
    with open('./private_smtp.txt', 'r') as smtpPassFile:
      return str.strip(smtpPassFile.read())

  def _get_content(self):
    html_template = Template(Path('./index.html').read_text())
    return html_template.substitute({'name': '吴仙杰', 'me': 'Jason Wu'})

  def _create_email(self):
    email = EmailMessage()
    email['from'] = 'wuxianjiezh@163.com'
    email['to'] = 'wuxianjiezh@hotmail.com'
    email['subject'] = '学海无崖'

    email.set_content(self._get_content(), 'html')

    return email


if __name__ == '__main__':
  sender = EmailSender()
  sender.send_email()
