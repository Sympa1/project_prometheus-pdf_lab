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
    def write_to_log(message: str, log_file_name: str = "error.log"):
        """Schreibt mit Zeitstempeln, einen String in eine \"Log\" Datei. Ist eine statische Methode, da sie nicht auf
        Instanzvariablen zugreift.

        :param str message: Die zu protokollierende Nachricht.
        :param str log_file_name: Der Name der Protokolldatei, standardmäßig "error.log".
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"
        with open(log_file_name, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def load_config(self):
        """Liest die config.json ein. Wenn die Datei nicht existiert, wird eine neue erstellt mit Standardwerten.
        """
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            # default Werte wenn die Datei nicht existiert
            self.data = {
                "debug": False,
                "theme": "dark",
                "window_width": 1130,
                "window_height": 757,       
            }
            self.save_config()

            # Fehlerprotokoll schreiben
            self.write_to_log("Config.json existiert nicht." + str(e))
            self.config_created = True

    def save_config(self):
        """Speichert die aktuelle Konfiguration in der config.json."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_config(self, key: str) -> int | str | bool | float | None:
        """Gibt den Wert für den angegebenen Schlüssel zurück, oder None, wenn der Schlüssel nicht existiert.

        :param str key: Der Schlüssel, dessen Wert abgerufen werden soll.
        :return int | str | bool | float | None: Der Wert für den angegebenen Schlüssel.
        """
        return self.data.get(key)

    def set_config(self, key: str, value: str | int | bool):
        """Setzt den Wert für den angegebenen Schlüssel und speichert die config.json."""
        self.data[key] = value
        self.save_config()