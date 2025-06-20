from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PdfMerger:
    def __init__(self):
        self.merger = PdfMerger()

    def add_file(self, file_path):
        self.merger.append(file_path)

    def merge_files(self, output_path):
        self.merger.write(output_path)
        self.merger.close()

    def get_page_count(self, file_path):
        reader = PdfReader(file_path)
        return len(reader.pages)

    def extract_text(self, file_path):
        reader = PdfReader(file_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return "\n".join(text)