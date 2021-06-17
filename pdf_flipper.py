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

print('Your file has {} pages, please select from what and to what page u want to rotate'.format(pdfile.numPages))
print('Use "START,END"\n')
pages=input().split(',')
print('Please select in degrees how u want to rotate the file (negative numbers are counter-clockwise first)\n')
rotation=input()

pdfwriter= PyPDF2.PdfFileWriter()
# i adopts the value of either 0, or 1, its kind of hard to read, but setdefault()
# returns a value, not the dictionary, so its a kind of different "if"
i= {'-': 0}.setdefault(rotation[0], 1)
r= input('Is every page rotated the same way? (y,n)')
if r == 'n':
    if "180" in rotation:
        flip= 1
        for x in range(pdfile.numPages):
            page=pdfile.getPage(x)
            c_wise=  {1: page.rotateClockwise, 0: page.rotateCounterClockwise}
            if x >= (int(pages[0])-1) and x <= (int(pages[1])-1) and flip ==  1:
                # rotating 180 counter clockwise and clockwise are the same.
                c_wise[i](abs(int(rotation)))
                flip = 0
            else:
                flip = 1
            #For some reason this causes a bug (tried to flip pages 50 to 58, but it
            # always skips page number 50)
            # if flip == 1:
            #     flip = 0
            # else:
            #     flip = 1
            pdfwriter.addPage(page)
    else:
        for x in range(pdfile.numPages):
            page=pdfile.getPage(x)
            c_wise=  {1: page.rotateClockwise, 0: page.rotateCounterClockwise}
            if x >= (int(pages[0])-1) and x <= (int(pages[1])-1):
                c_wise[i](abs(int(rotation)))
                if i == 0:
                    i=1
                else:
                    i=0
            pdfwriter.addPage(page)
elif r == 'y':
    for x in range(pdfile.numPages):
        page=pdfile.getPage(x)
        c_wise=  {1: page.rotateClockwise, 0: page.rotateCounterClockwise}
        if x >= (int(pages[0])-1) and x <= (int(pages[1])-1):
            c_wise[i](abs(int(rotation)))
        pdfwriter.addPage(page)

result= open(Path.cwd()/'results'/file, 'wb')
pdfwriter.write(result)

print('done')

op_file.close()
result.close()
