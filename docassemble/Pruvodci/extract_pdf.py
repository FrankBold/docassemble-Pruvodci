import io
import requests
import pikepdf
from docassemble.base.util import path_and_mimetype, ocr_file, DAObject, DAFile

def extract_pdf_pages(original, otazky, pages_to_remove, obec):
    # Open the input PDF files
    pdf_file = pikepdf.open(original.path())
    pdf_otazky = pikepdf.open(otazky.path())
    
    pdf_writer = pikepdf.Pdf.new()
    
    # Copy all pages except the ones specified for removal
    for page_num, page in enumerate(pdf_file.pages):
        if page_num not in pages_to_remove:
            if page_num == 18:
                for page_otazky in pdf_otazky.pages:
                    pdf_writer.pages.append(page_otazky)
            
            pdf_writer.pages.append(page)

    # Set the PDF to be read-only
    pdf_writer.save('temp.pdf')
    pdf_temp = pikepdf.open('temp.pdf')
    pdf_temp.save('final.pdf', encryption=pikepdf.Encryption(owner='', user='', R=4, allow=pikepdf.Permissions.none))
    
    edited_io = io.BytesIO()
    
    # Save the edited PDF to the BytesIO stream
    with open('final.pdf', 'rb') as f:
        edited_io.write(f.read())
    
    edited_io = io.BytesIO()
    
    # Save the edited PDF to the BytesIO stream
    pdf_writer.save(edited_io)
    
    # Move the cursor to the beginning of the BytesIO stream
    edited_io.seek(0)
    
    files = {
        'file': ('Analyza_' + obec + '.pdf', edited_io, 'application/pdf'),
    }

    # Make a POST request to your specified URL
    output = requests.post('https://hook.eu1.make.com/wske766bh4n63ym2389icfkshr8hsuik', files=files)
    
    return output.text
