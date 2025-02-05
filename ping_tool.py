import os
import platform
import time
import keyboard
from colorama import Fore, init
from clear_screen import clear_screen
from log_to_file import log_to_file

def ping_host():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "📡 PING-TEST".center(50))
    print(Fore.CYAN + "=" * 50)

    host = input(Fore.YELLOW + "\n🔹 Geben Sie die IP-Adresse oder den Hostnamen ein: ").strip()

    if not host:
        print(Fore.RED + "❌ Keine gültige Eingabe! Bitte eine IP-Adresse oder Host eingeben.")
        return

    try:
        pings_per_second = int(input(Fore.YELLOW + "\n🔹 Geben Sie die Anzahl der Pings pro Sekunde ein: ").strip())
        if pings_per_second <= 0:
            raise ValueError
    except ValueError:
        print(Fore.RED + "❌ Ungültige Eingabe. Standardmäßig wird 1 Ping pro Sekunde verwendet.")
        pings_per_second = 1

    # Kompatibilität für Windows und Linux
    count = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    dev_null = "nul" if platform.system().lower() == "windows" else "/dev/null"

    print(Fore.GREEN + f"\n🌍 Beginne mit dem Pingen von {host} (Drücke 'X' zum Hauptmenü)...\n")

    while True:
        # Ping-Befehl ausführen
        response = os.system(f"ping {count} {host} > {dev_null} 2>&1")

        if response == 0:
            current_result = Fore.GREEN + f"{host} is online!"
        else:
            current_result = Fore.RED + f"{host} is offline"
            print(Fore.RED + "⚠️ IP nicht erreichbar!")

        # Zeige das aktuelle Ping-Ergebnis an und speichere es ins Log
        print(Fore.WHITE + current_result)
        log_to_file("ping", current_result)

        # Prüfe, ob 'X' gedrückt wurde, um zum Hauptmenü zurückzukehren
        if keyboard.is_pressed("x"):
            print(Fore.WHITE + "\n🔚 Zurück zum Hauptmenü...")
            break

        time.sleep(1 / pings_per_second)  # Pause zwischen den Pings

