
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PdfUtility:
    def __init__(self):
        self.merger = PdfMerger()

    def get_page_count(self, file_path): # TODO: könnte ich später noch für anzeigen im GUI verwenden
        reader = PdfReader(file_path)
        return len(reader.pages)

    def extract_text(self, file_path): # TODO: könnte ich später noch für anzeigen im GUI verwenden
        reader = PdfReader(file_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return "\n".join(text)

    def merge_pdf(input_files, output_file):
        """Merged mehrere PDF-Dateien in eine einzelne PDF-Datei und speichert sie unter dem angegebenen Dateipfad."""
        writer = PdfWriter()
        for file in input_files:
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_file, "wb") as f:
            writer.write(f)

    def split_pdf(input_file, output_file1, output_file2, split_at):
        """Teilt eine PDF-Datei an der angegebenen Seitenzahl in zwei Dateien mit benutzerdefinierten Pfaden."""
        """Teilt eine PDF-Datei an der angegebenen Seitenzahl in zwei Dateien."""
        reader = PdfReader(input_file)
        total_pages = len(reader.pages)

        # Erster Teil: Seiten 1 bis split_at
        writer1 = PdfWriter()
        for i in range(split_at):
            writer1.add_page(reader.pages[i])
        with open(output_file1, "wb") as f:
            writer1.write(f)

        # Zweiter Teil: Seiten split_at+1 bis Ende
        writer2 = PdfWriter()
        for i in range(split_at, total_pages):
            writer2.add_page(reader.pages[i])
        with open(output_file2, "wb") as f:
            writer2.write(f)

        return [output_file1, output_file2]

