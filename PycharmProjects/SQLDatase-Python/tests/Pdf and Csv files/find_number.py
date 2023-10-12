import re

import PyPDF2

file = open('Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfReader(file)
print(pdf.numPages)
pattern = r'\d{3}'
all_text = ''

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text
for match in re.finditer(pattern, all_text):
    print(match)

pattern = r'\d{3}.\d{3}.\d{4}'
for n in range(pdf.numPages):

    page = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern, page_text)

    if match:
        print(match.group())
