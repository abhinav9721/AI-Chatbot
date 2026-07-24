import os
from pypdf import PdfReader
from docx import Document

# ==========================
# Maximum PDF Pages
# ==========================

MAX_PAGES = 50


# ==========================
# Read TXT File
# ==========================

def read_txt(file):

    try:

        file.seek(0)

        text = file.read().decode("utf-8")

        return text

    except Exception as e:

        print("TXT Error:", e)

        return None


# ==========================
# Read PDF File
# ==========================

def read_pdf(file):

    try:

        file.seek(0)

        reader = PdfReader(file)

        # Check Page Limit
        if len(reader.pages) > MAX_PAGES:
            return "PAGE_LIMIT_EXCEEDED"

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:

        print("PDF Error:", e)

        return None


# ==========================
# Read DOCX File
# ==========================

def read_docx(file):

    try:

        file.seek(0)

        document = Document(file)

        text = ""

        for paragraph in document.paragraphs:

            text += paragraph.text + "\n"

        return text

    except Exception as e:

        print("DOCX Error:", e)

        return None


# ==========================
# Extract Text
# ==========================

def extract_text(uploaded_file):

    try:

        extension = os.path.splitext(
            uploaded_file.name
        )[1].lower()

        if extension == ".txt":

            return read_txt(uploaded_file)

        elif extension == ".pdf":

            return read_pdf(uploaded_file)

        elif extension == ".docx":

            return read_docx(uploaded_file)

        else:

            return None

    except Exception as e:

        print("Extract Error:", e)

        return None