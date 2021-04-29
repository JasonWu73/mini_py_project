import os
import sys

from PIL import Image

from basic import make_output_dir


def get_params():
  """
  从终端读取2-元组参数。

  :return: (源目录, 输出目录)
  """

  if len(sys.argv) < 3:
    raise ValueError('运行脚本时还需指定两个参数，参数1：源目录，参数：输出目录')

  src_dir, out_dir = sys.argv[1:3]

  if not os.path.exists(src_dir):
    raise ValueError('源目录不存在或不可读')

  return src_dir, out_dir


def convert_to_png(src_dir, dest_dir):
  """
  将源目录中的所有图片转换为 png，并写入到输出目录中。

  :param src_dir: 源图片所在目录
  :param dest_dir: 生成图片的目录
  """

  for filename in os.listdir(src_dir):
    # 因为生成目录可能是在源目录下，故需过滤生成目录
    src_img = f'{src_dir}/{filename}'
    if os.path.isdir(src_img):
      continue

    png_img = f'{dest_dir}/{os.path.splitext(filename)[0]}.png'

    with Image.open(src_img) as image:
      image.save(png_img, 'PNG')
      print(f'{src_img} -> {png_img}')


if __name__ == '__main__':
  src, out = get_params()
  make_output_dir(out)
  convert_to_png(src, out)
