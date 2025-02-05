from datetime import datetime
import os


def log_to_file(func_name, message):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Erstellt 'logs/' falls nicht vorhanden

    log_filename = f"{log_dir}/{func_name}_{datetime.now().strftime('%Y-%m-%d')}.log"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] {message}\n"

    # Öffne die Datei mit UTF-8, um Unicode-Probleme zu vermeiden
    with open(log_filename, "a", encoding="utf-8") as log_file:
        log_file.write(log_message)

    print(f"📜 Log gespeichert: {log_filename}")  # Optional für Debugging