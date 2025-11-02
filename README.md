# Project Prometheus - PDF Lab

PDF Lab ist ein Tool zum mergen und splitten von PDFs. Außerdem kann man PDFs ver- und entschlüsseln. 

## Funktionen
- PDF mergen
- PDF splitten
- PDF ver- und entschlüsseln

## Roadmap
- Multithreading um parallele Funktionen auszuführen
- Progressbars für alle Funktionen
- Passwort Sicherheitsanalyse mit Echtzeit-Bewertung in Form einer Anzeige wie sicher das gewählte Passwort ist
- Ausschluss schwacher Passwörter (123456789, hallo, etc.)
- Verlinkung zum GitHub Repository

## Lessons Learned
Eine kleine Herausforderung war es für mich das UI zu gestalten. CustomTkinter bietet aber gute Möglichkeiten ein Modernes UI zu gestalten. 
Eine größere Herausforderung, weil ich das noch nicht gemacht habe, war es, die Settings (Fenstergröße und Theme) nachhaltig zu speichern. Die Möglichkeit wollte ich möglichst simpel halten, was mir auch gelungen ist. Im Großen und Ganzen habe ich einiges dazu gelernt und daher bewerte ich das Projekt als Erfolg. 
Weitere spannende Ideen, die ich gerne umsetzen möchte, habe ich in der Roadmap beschrieben.

## Voraussetzungen
- Python 3.8+
- pip
- virtualenv (empfohlen) 

## Verzeichnisstruktur
```
.
├── data/
│   └── img
│       └── ...
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
1. Dieses Repository klonen:
   ```
   git clone https://github.com/Sympa1/PyPDFCrafter
   ```
2. In das Repository Verzeichnis navigieren:
   ```
   cd Project_Prometheus-PDF_Lab
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

## Bekannte Probleme
- Keine bekannten Probleme

## Build-Tools
- PyInstaller 6.1.0
```shell
pyinstaller --onefile --windowed --icon=data/img/document.ico --hidden-import=customtkinter --add-data "data/img;data/img" src/main.py
```

## Lizenz
Dieses Projekt ist unter der GPL-3.0 lizenziert - siehe die [LICENSE](LICENSE)-Datei für Details.
