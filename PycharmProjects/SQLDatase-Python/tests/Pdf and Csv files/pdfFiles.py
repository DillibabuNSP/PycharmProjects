import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)
page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)
f.close()

fb = open('Working_Business_Proposal.pdf', 'rb')
pdf_readers = PyPDF2.PdfFileReader(fb)
first_page = pdf_readers.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
fb.close()
pdf_output.close()

fc = open('Working_Business_Proposal.pdf', 'rb')
pdf_Text = []
pdf_readerss = PyPDF2.PdfFileReader(fc)
for num in range(pdf_readerss.numPages):
    page = pdf_readerss.getPage(num)
    pdf_Text.append(page.extractText())

print(pdf_Text[1])