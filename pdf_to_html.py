# Python script that takes a PDF file and converts it to HTML
import pdfplumber
import os


# function to convert pdf to html
def pdf_to_html(file_path):
    with pdfplumber.open(file_path) as pdf:
        # get all the pages in the pdf
        pages = pdf.pages
        html_text = "<html><body>"
        for page in pages:
            # extract text from each page
            text = page.extract_text()
            # add the text to the html_text variable
            html_text += text
        html_text += "</body></html>"
    return html_text


# get the file path


file_path = input("Enter the file path:")
# check if the file exists
if os.path.isfile(file_path):
    # call the pdf_to_html function and get the html text
    html_text = pdf_to_html(file_path)
    # write the html text to a file
    with open("output.html", "w") as f:
        f.write(html_text)
    print("File converted and saved as output.html")
else:
    print("File not found")
