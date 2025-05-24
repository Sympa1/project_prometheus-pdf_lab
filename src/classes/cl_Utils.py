import os
from datetime import datetime

class Utils():
    @staticmethod
    def write_to_log(self, message, log_file_name="error.log"):
        # Pfad zur übergeordneten Ebene der Datei
        script_dir = os.path.dirname(os.path.abspath(__file__))  # z. B. src/
        parent_dir = os.path.dirname(script_dir)  # z. B. PyPDFCrafter/

        log_file_path = os.path.join(parent_dir, log_file_name)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {message}\n"

        with open(log_file_path, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    # config schreiben

    # config lesen

    # fehler log schreiben
