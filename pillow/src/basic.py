import os
from pathlib import Path

from PIL import Image, ImageFilter


def make_output_dir(output_dir):
  """
  若输出目录不存在，则创建；否则，不做任何事

  :param output_dir: 输出图片所在目录
  """

  if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def blur(img_obj, img_root_path):
  """
  添加模糊滤镜。生成新图片 `{img_root_path}_blur.png`。

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  filtered_img_path = f'{img_root_path}_blur.png'
  filtered_img = img_obj.filter(ImageFilter.BLUR)
  filtered_img.save(filtered_img_path, 'PNG')

  print(f'模糊滤镜图片：{filtered_img_path}')
  filtered_img.show()


def grey(img_obj, img_root_path):
  """
  颜色转换，彩色 -> 灰度影像。生成新图片 `{img_root_path}_grey.png`。

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  converted_img_path = f'{img_root_path}_grey.png'
  converted_img = img_obj.convert('L')
  converted_img.save(converted_img_path, 'PNG')

  print(f'灰度影像：{converted_img_path}')
  converted_img.show()


def rotate(img_obj, img_root_path):
  """
  旋转图片。生成新图片 `{img_root_path}_rotate.png`

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  rotated_img_path = f'{img_root_path}_rotate.png'
  rotated_img = img_obj.rotate(45)
  rotated_img.save(rotated_img_path, 'PNG')

  print(f'旋转后图片：{rotated_img_path}')
  rotated_img.show()


def resize(img_obj, img_root_path):
  """
  非等比例缩放图片。生成新图片 `{img_root_path}_resize.png`

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  resized_img_path = f'{img_root_path}_resize.png'
  resized_img = img_obj.resize((180, 180))
  resized_img.save(resized_img_path, 'PNG')

  print(f'非等比例缩放后图片：{resized_img_path}')
  resized_img.show()


def thumbnail(img_obj, img_root_path):
  """
  生成等比例缩略图。生成新图片 `{img_root_path}_thumbnail.png`

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  thumbnail_path = f'{img_root_path}_thumbnail.jpg'
  copied_img = img_obj.copy()  # `thumbnail()` 会修改原图，故拷贝一份做缩略图
  copied_img.thumbnail((180, 180))
  copied_img.save(thumbnail_path, 'JPEG')

  print(f'等比例缩略图：{thumbnail_path}')
  img_obj.show()


def crop(img_obj, img_root_path):
  """
  裁剪图片。生成新图片 `{img_root_path}_crop.png`

  :param img_obj: `PIL.Image.Image`
  :param img_root_path: 文件根路径（不含后缀及 `.`）
  """

  box = (100, 100, 400, 400)
  cropped_img_path = f'{img_root_path}_crop.png'
  cropped_img = img_obj.crop(box)
  cropped_img.save(cropped_img_path, 'PNG')

  print(f'裁剪后图片：{cropped_img_path}')
  cropped_img.show()


if __name__ == '__main__':
  img_path = '../images/pikachu.jpg'

  out_dir = os.path.join(os.path.dirname(img_path), 'basic_py')
  make_output_dir(out_dir)

  file_name_no_ext = Path(img_path).stem
  no_ext_img_path = os.path.join(out_dir, file_name_no_ext)

  with Image.open(img_path) as img:
    blur(img, no_ext_img_path)
    grey(img, no_ext_img_path)
    rotate(img, no_ext_img_path)
    resize(img, no_ext_img_path)
    thumbnail(img, no_ext_img_path)
    crop(img, no_ext_img_path)
