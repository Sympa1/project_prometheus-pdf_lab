import os
import json

from datetime import datetime
from gui.cl_Messagebox import Messagebox

class Utils():
    """Hilfsklasse."""
    def __init__(self, filename = "config.json"):
        self.filename = filename
        self.data = {}
        self.config_created = False  # <--- Flag hinzufügen
        self.load_config() # lädt automatisch die Config beim erstellen des Objektes

    @staticmethod # das später noch anpassen
    def write_to_log(message, log_file_name="error.log"):
        """Schreibt mit Zeitstempel, einen String in eine \"Log\" Datei."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"

        with open(log_file_name, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def load_config(self):
        """Liest die Configdatei ein."""
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            # Default values wenn datei nicht existiert
            self.data = {
                "debug": False,
                "theme": "dark",
                "window_width": 800,
                "window_height": 600
            }
            self.save_config()

            # Fehlerprotokoll schreiben
            self.write_to_log("Config.json existiert nicht." + str(e))
            self.config_created = True

    def save_config(self):
        """Speichere config in Datei."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_config(self, key):
        """Hole wert."""
        return self.data.get(key)
    
    def set_config(self, key, value):
        """Setze wert und speichere."""
        self.data[key] = value
        self.save_config()