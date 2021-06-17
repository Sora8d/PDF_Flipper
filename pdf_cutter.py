import PyPDF2
import os

from pathlib import Path

all_files= os.listdir(Path.cwd()/'pdfs')
for x in range(len(all_files)):
    print('{}: {}'.format(x, all_files[x]))
print('Please choose the number of the file u want to rotate: ')
file= all_files[int(input())]
op_file= open(Path.cwd()/'pdfs'/file, 'rb')
pdfile= PyPDF2.PdfFileReader(op_file)

print('Your file has {} pages, please select from what and to what page u want to cut'.format(pdfile.numPages))
print('Use "START,END"\n')
pages=input().split(',')

pdfwriter= PyPDF2.PdfFileWriter()

for x in range(int(pages[0])-1, int(pages[1])):
    page=pdfile.getPage(x)
    pdfwriter.addPage(page)

result= open(Path.cwd()/'results'/file, 'wb')
pdfwriter.write(result)

print('done')

op_file.close()
result.close()
