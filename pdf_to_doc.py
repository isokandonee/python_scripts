# Python script that takes a PDF file and converts it to DOC
from docx import Document

def pdf_to_doc(file_path):
    with pdfplumber.open(file_path) as pdf:
        pages = pdf.pages
        doc = Document()
        for page in pages:
            text = page.extract_text()
            doc.add_paragraph(text)
    return doc

file_path = input("Enter the file path:")
if os.path.isfile(file_path):
    doc = pdf_to_doc(file_path)
    doc.save("output.docx")
    print("File converted and saved as output.docx")
else:
    print("File not found")
