# PyPDFCrafter
PyPDFCrafter: Die All-in-One PDF-Lösung für modernes Dokumentenmanagement. Verbinde, trenne und schütze deine PDFs mit wenigen Klicks – effizient, intuitiv und zuverlässig. 

## Überblick
PyPDFCrafter dient der vereinfachten Bearbeitung von PDF-Dokumenten und ermöglicht grundlegende Operationen wie das Zusammenfügen mehrerer PDFs, das Aufteilen von Dokumenten und die Verschlüsselung zum Schutz vertraulicher Informationen. Die benutzerfreundliche CustomTkinter-Oberfläche macht komplexe PDF-Bearbeitungen auch für Einsteiger zugänglich.

## Funktionen
- PDF-Zusammenführung
- PDF-Aufteilung
- PDF-Verschlüsselung
- Benutzerfreundliche Oberfläche
- Drag & Drop-Unterstützung
- Vorschau-Funktion
- Plattformübergreifend

### Bedienungsanleitung
1. PDF-Dateien auswählen
2. Gewünschte Operation wählen (Zusammenfügen, Aufteilen, Verschlüsseln)
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
│   ├── main.py
│   └── starter.sh
├── .venv/
│   ├── ...
|   └── ...
├── .git/
├── .gitignore
├── config.json
├── error.log
├── LICENSE
├── README.md
└── requirements.txt
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
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Umgebungsvariablen
Die Anwendung unterstützt optionale Umgebungsvariablen für erweiterte Konfigurationen. Diese können in einer `.env`-Datei im Hauptverzeichnis gespeichert werden.

Beispiel für eine `.env`-Datei:
```
# Ausgabepfad für verarbeitete PDFs
OUTPUT_DIR=/pfad/zum/ausgabeverzeichnis

# UI-Einstellungen
THEME_MODE=dark  # oder "light", "system"
PRIMARY_COLOR=#1E88E5
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

### Als ausführbare Datei erstellen
```bash
# Mit PyInstaller
pyinstaller --onefile --windowed --icon=assets/icon.png main.py
```

## Bekannte Probleme
- Keine bekannten Probleme

## Abhängigkeiten
- CustomTkinter 5.2.0
- PyPDF2 3.0.1
- Pillow 10.1.0
- PyInstaller 6.1.0 (optional, für ausführbare Dateien)

## Lizenz
Dieses Projekt ist unter der GPL-3.0 lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.

## Screenshots
*(Hier könnten Sie Screenshots der Anwendung einfügen)*