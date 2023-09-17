import io
import PyPDF2
import requests
from docassemble.base.util import path_and_mimetype, ocr_file, DAObject, DAFile

def extract_pdf_pages(original, otazky, pages_to_remove):
  
  pdf_file = open(original.path(), 'rb')
  pdf_otazky = open(otazky.path(), 'rb')
  
  pdf_reader = PyPDF2.PdfFileReader(pdf_file)
  otazky_reader = PyPDF2.PdfFileReader(pdf_otazky)
  
  pdf_writer = PyPDF2.PdfFileWriter()

  # Copy all pages except the ones specified for removal
  for page_num in range(pdf_reader.numPages):
    if page_num not in pages_to_remove:
      if page_num == 18:
        for page_num_o in range(otazky_reader.numPages):
          otazka = otazky_reader.getPage(page_num_o)
          pdf_writer.addPage(otazka)
        
      page = pdf_reader.getPage(page_num)        
      pdf_writer.addPage(page)
          
  edited_io = io.BytesIO()
    
  pdf_writer.write(edited_io)

  pdf_file.close()
  pdf_otazky.close()
    
  # Move the cursor to the beginning of the BytesIO stream
  edited_io.seek(0)
    
  files = {
  'file': ('filename.pdf', edited_io, 'application/pdf'),
  }

  output = requests.post('https://hook.eu1.make.com/wske766bh4n63ym2389icfkshr8hsuik', files=files)
    
  return output.text