import json
from datetime import datetime


class Utils:
    """Hilfsklasse."""
    def __init__(self, filename = "config.json"):
        self.filename = filename
        self.data = {}
        self.config_created = False  # Flag hinzufügen, um zu prüfen, ob die config.json neu erstellt wurde
        self.load_config() # lädt automatisch die config.json beim erstellen des Objektes

    @staticmethod # TODO: das später noch anpassen
    def write_to_log(message, log_file_name="error.log"):
        """Schreibt mit Zeitstempeln, einen String in eine \"Log\" Datei. Ist eine statische Methode, da sie nicht auf
        Instanzvariablen zugreift."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"
        with open(log_file_name, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def load_config(self):
        """Liest die config.json ein. Wenn die Datei nicht existiert, wird eine neue erstellt mit Standardwerten."""
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            # default Werte wenn die Datei nicht existiert
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
        """Speichert die aktuelle Konfiguration in der config.json."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_config(self, key):
        """Gibt den Wert für den angegebenen Schlüssel zurück, oder None, wenn der Schlüssel nicht existiert."""
        return self.data.get(key)
    
    def set_config(self, key, value):
        """Setzt den Wert für den angegebenen Schlüssel und speichert die config.json."""
        self.data[key] = value
        self.save_config()