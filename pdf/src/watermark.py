import PyPDF2


def add_watermark():
  with open(
      '../documents/twopage.pdf', 'rb') as template, open(
      '../documents/wtr.pdf', 'rb') as watermark, open('watermarked.pdf',
                                                       'wb') as file:
    template_reader = PyPDF2.PdfFileReader(template)
    watermark_reader = PyPDF2.PdfFileReader(watermark)
    watermark_page = watermark_reader.getPage(0)

    output = PyPDF2.PdfFileWriter()

    for i in range(template_reader.getNumPages()):
      template_page = template_reader.getPage(i)
      template_page.mergePage(watermark_page)
      output.addPage(template_page)

    output.write(file)


if __name__ == '__main__':
  add_watermark()
