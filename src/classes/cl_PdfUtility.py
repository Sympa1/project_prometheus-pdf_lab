
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PdfUtility:
    def __init__(self):
        self.merger = PdfMerger()

    def get_page_count(self, file_path: str) -> int:
        """Gibt die Anzahl der Seiten in einer PDF-Datei zurück.

        :param str file_path: Der Pfad zur PDF-Datei.
        :return int: Die Anzahl der Seiten in der PDF-Datei.
        """
        reader = PdfReader(file_path)
        return len(reader.pages)

    def merge_pdf(input_files: list[str], output_file: str):
        """Merged mehrere PDF-Dateien in eine einzelne PDF-Datei und speichert sie unter dem angegebenen Dateipfad.

        :param list[str] input_files: Die Pfade zu den Eingabe-PDF-Dateien.
        :param str output_file: Der Pfad zur Ausgabedatei.
        :return _type_: None
        """
        writer = PdfWriter()
        for file in input_files:
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)
        with open(output_file, "wb") as f:
            writer.write(f)

    def split_pdf(input_file: str, output_file1: str, output_file2: str, split_at: int):
        """Teilt eine PDF-Datei an der angegebenen Seitenzahl in zwei Dateien mit benutzerdefinierten Pfaden.

        :param str input_file: Der Pfad zur Eingabe-PDF-Datei.
        :param str output_file1: Der Pfad zur Ausgabedatei für den ersten Teil.
        :param str output_file2: Der Pfad zur Ausgabedatei für den zweiten Teil.
        :param int split_at: Die Seitenzahl, an der die PDF geteilt werden soll.
        :return _type_: None
        """
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

    def encrypt_pdf(input_file: str, output_file: str, password: str):
        """Verschlüsselt eine PDF-Datei mit einem Passwort.

        :param str input_file: Der Pfad zur Eingabe-PDF-Datei.
        :param str output_file: Der Pfad zur Ausgabedatei.
        :param str password: Das Passwort zum Verschlüsseln der PDF-Datei.
        :return _type_: None
        """
        reader = PdfReader(input_file)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(user_password=password, use_128bit=True)
        with open(output_file, "wb") as f:
            writer.write(f)