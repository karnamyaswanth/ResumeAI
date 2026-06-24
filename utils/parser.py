from PyPDF2 import PdfReader
from docx import Document


def extract_text(uploaded_file):

    text = ""

    if uploaded_file.name.endswith(".pdf"):

        pdf = PdfReader(uploaded_file)

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted


    elif uploaded_file.name.endswith(".docx"):

        doc = Document(uploaded_file)

        for para in doc.paragraphs:

            text += para.text + "\n"

    return text