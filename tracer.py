import subprocess
import threading
import time
from sys import platform
import platform
import keyboard
from colorama import Fore
import os
from clear_screen import clear_screen
from log_to_file import log_to_file


# 🌍 Traceroute (Grün für Netzwerkverbindung)
def traceroute():
    clear_screen()
    host = input(Fore.YELLOW + "Geben Sie die IP-Adresse oder den Hostnamen für Traceroute ein: ")

    print(Fore.CYAN + "[INFO] Drücken Sie Strg + X, um den Traceroute abzubrechen.")

    command = "tracert" if platform.system().lower() == "windows" else "traceroute"

    print(Fore.GREEN + f"Starte Traceroute für {host}...")

    # Funktion zum Ausführen des Traceroutes

    def run_traceroute(process):
        try:
            # Starten des Traceroute-Prozesses mit mbcs Encoding für Windows
            for line in process.stdout:
                print(Fore.CYAN + line.strip())  # Farbig für die Ausgabe
            process.communicate()  # Warten, bis der Prozess beendet ist
        except Exception as e:
            print(Fore.RED + f"Fehler beim Ausführen von Traceroute: {e}")

    # Funktion zum Abfangen von Strg + X
    def check_abort(process):
        while True:
            if keyboard.is_pressed('ctrl+x'):  # Überprüft, ob Strg + X gedrückt wurde
                print(Fore.YELLOW + "\n[INFO] Traceroute wird abgebrochen... Drücken Sie 'Enter', um fortzufahren.")
                process.terminate()  # Beende den Traceroute-Prozess sicher
                break
            time.sleep(0.1)  # Kurze Pause, um CPU-Last zu verringern

    # Starten des Traceroute-Prozesses mit mbcs Encoding für Windows
    process = subprocess.Popen([command, host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                               encoding='mbcs')

    # Starten des Traceroute-Threads, der die Ausgabe verarbeitet
    traceroute_thread = threading.Thread(target=run_traceroute, args=(process,))
    traceroute_thread.start()

    # Starten eines weiteren Threads, der auf Strg + X wartet
    abort_thread = threading.Thread(target=check_abort, args=(process,))
    abort_thread.start()

    # Auf Beendigung des Traceroute-Prozesses und Abbruch-Threads warten
    traceroute_thread.join()  # Warten bis der Traceroute-Thread beendet ist
    abort_thread.join()  # Warten bis der Abbruch-Thread beendet ist

    log_to_file("traceroute", f"Executed traceroute for: {host}")