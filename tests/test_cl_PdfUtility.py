from classes.cl_PdfUtility import PdfUtility
import os

# TODO: muss mit folgenden Befehl aus dem Hauptverzeichnis aus aufgerufen werden:
# PYTHONPATH=src python tests/test_cl_PdfUtility.py

class TestPdfUtility():
    """Testklasse für die PdfUtility-Klasse."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Konstruktor übernimmt die Aufgaben von setUp
        self.pdf_util = PdfUtility()
        test_dir = os.path.dirname(__file__)
        self.pdf1 = os.path.join(test_dir, "test1.pdf")
        self.pdf2 = os.path.join(test_dir, "test2.pdf")
        self.output_merged = "testMerged.pdf"
        self.output_dir = "."

    def test_merge_pdf(self):
        """Testet das Zusammenführen von zwei PDF-Dateien."""
        PdfUtility.merge_pdf([self.pdf1, self.pdf2], self.output_merged)

    def test_split_pdf(self):
        """Testet das Teilen einer PDF-Datei in zwei Teile."""
        # Erzeuge eine gemergte Datei, falls sie noch nicht existiert
        if not os.path.exists(self.output_merged):
            PdfUtility.merge_pdf([self.pdf1, self.pdf2], self.output_merged)
        result = PdfUtility.split_pdf(self.output_merged, self.output_dir, 1)

    def tearDown(self):
        """Löscht die Test-PDF-Dateien nach den Tests."""
        for fname in [self.pdf1, self.pdf2, self.output_merged, "part1.pdf", "part2.pdf"]:
            if os.path.exists(fname):
                os.remove(fname)   
            print(f"Deleted {fname} if it existed.")


if __name__ == "__main__":
    test = TestPdfUtility()
    #test.test_merge_pdf()
    test.test_split_pdf()
    #test.tearDown()