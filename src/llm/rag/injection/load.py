import PyPDF2

def read_pdf_text(file_path: str):
    text = ""
    with open (file_path, "rb") as file:
        pdf_reader = PyPDF2.PDFReader(file)
        for page in pdf_reader.pages:
            test+= page.extract_text()+"\n"
    return text

def read_text(file_path: str):
    with open (file_path, "r",encoding="utf-8") as file:
        return file.read()