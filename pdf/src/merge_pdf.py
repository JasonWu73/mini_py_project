import sys
from pathlib import Path

import PyPDF2


def get_files():
  """获取所有需要合并的 PDF 文件及最终输出文件路径"""
  if len(sys.argv) < 3:
    raise ValueError('运行脚本时还需指定至少两个参数，'
                     '参数1~n-1：需要合并的文件，参数n：输出文件')

  files = (sys.argv[i] for i in range(1, len(sys.argv) - 1))
  output_file = sys.argv[-1]

  return files, output_file


def merge_pdf():
  """按顺序合并所有 PDF 文件"""
  files, output_file = get_files()

  merger = PyPDF2.PdfFileMerger()
  for file_path in files:
    merger.append(file_path, f'合并自 {Path(file_path).stem}')

  merger.write(output_file)


if __name__ == '__main__':
  merge_pdf()
