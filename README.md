# PyPDFCrafter

PyPDFCrafter dient der vereinfachten Bearbeitung von PDF-Dokumenten und ermöglicht grundlegende Operationen wie das Zusammenfügen mehrerer PDFs, das Aufteilen von Dokumenten und die Verschlüsselung zum Schutz vertraulicher Informationen.

## Funktionen
- PDF-Zusammenführung
- PDF-Aufteilung
- PDF-Verschlüsselung
- Benutzerfreundliche Oberfläche
- Plattformübergreifend

## Roadmap
- Passwort-Sicherheitsanalyse mit Echtzeit-Bewertung
- Multithreading für bessere Performance bei großen Dateien
- Fortschrittsanzeige (Progressbars) für alle Operationen
- Ausschluss schwacher Passwörter (123456789, hallo, etc.)
- Anzeige wie sicher das gewählte Passwort ist
- Verlinkung zum GitHub Repository

## Bedienungsanleitung
1. Gewünschte Operation wählen (Zusammenfügen, Aufteilen, Verschlüsseln)
2. PDF-Dateien auswählen
3. Zieloptionen konfigurieren (Ausgabeverzeichnis, Passwort, etc.)
4. "Ausführen" klicken und PDF-Bearbeitung starten

## Voraussetzungen
- Python 3.8+
- pip
- virtualenv (empfohlen) 

## Verzeichnisstruktur
```
.
├── data/
│   └── img
│       └── icon.?
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   └── windows.py
│   ├── classes/
│   │   ├── __init__.py
│   │   ├── merger.py
│   │   ├── splitter.py
│   │   └── encryptor.py
│   └── main.py
├── .venv/
│   ├── ...
|   └── ...
├── tests/
│   ├── test1.pdf
│   ├── test2.pdf
│   ├── testMerged.pdf
│   └── test_cl_PdfUtility.py
├── .git/
├── .gitignore
├── config.json
├── error.log
├── LICENSE
├── README.md
├── requirements.txt
└── starter.sh
```

## Installation
1. Klone dieses Repository:
   ```
   git clone https://github.com/Sympa1/PyPDFCrafter
   ```
2. Navigiere in das Verzeichnis:
   ```
   cd PyPDFCrafter
   ```
3. Virtuelles Environment einrichten:
   ```bash
   # Windows
   python -m venv .venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## .gitignore
Die folgende `.gitignore`-Datei wird verwendet:
```
# Umgebungsvariablen-Dateien
.env
**/.env

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Ausgabedateien
output/

# System-Dateien
.DS_Store
Thumbs.db
```

## Verwendung
### Anwendung starten
```bash
# Mit aktiviertem virtualenv
python main.py
```

## Bekannte Probleme
- Keine bekannten Probleme

## Abhängigkeiten
- CustomTkinter 5.2.0
- PyPDF2 3.0.1
- Pillow 10.1.0
- PyInstaller 6.1.0 (optional, für ausführbare Dateien)
   --> `pyinstaller --onefile --windowed --icon=data/img/document.ico --hidden-import=customtkinter --add-data "data/img;data/img" src/main.py`

## Lizenz
Dieses Projekt ist unter der GPL-3.0 lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.
