import PyPDF2
import sys
import os
import time


# merges all files found in input_file(accepted as argument)
def combine_pdf_files():
    input_file = "put_your_pdf_files"
    files = os.listdir(input_file)
    merger = PyPDF2.PdfFileMerger()

    for pdf in files:
        merger.append(input_file + "/" + pdf)
    merger.write("combinedPdf.pdf")  # creates new combined file
    print("created combinedPdf.pdf")
    time.sleep(2)

    watermark("combinedPdf.pdf")  # launch watermark func


# add watermark on each
def watermark(input_file):
    input_pdf = PyPDF2.PdfFileReader(open(input_file, "rb"))
    watermark_file = os.listdir("put_your_watermark")[0]
    watermark_pdf = PyPDF2.PdfFileReader(
        open("put_your_watermark/" + watermark_file, "rb"))
    output = PyPDF2.PdfFileWriter()

    for i in range(input_pdf.getNumPages()):  # put watermark on each page
        page = input_pdf.getPage(i)
        page.mergePage(watermark_pdf.getPage(0))
        output.addPage(page)

        with open("watermarked.pdf", "wb") as file:  # final output file
            output.write(file)

    os.remove("combinedPdf.pdf")  # finally remove unecessary document
    print("removed previous file")
    print("your watermarked.pdf was created!")


if __name__ == "__main__":
    combine_pdf_files()
