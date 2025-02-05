import speedtest
import threading
from colorama import Fore, init
from clear_screen import clear_screen
from animated_loader import animated_loader
from log_to_file import log_to_file


def run_speedtest():
    init(autoreset=True)  # Initialize colorama for colored output

    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🚀 SPEEDTEST".center(50))
    print(Fore.CYAN + "=" * 50)

    try:
        st = speedtest.Speedtest()
    except Exception as e:
        print(Fore.RED + f"❌ Fehler beim Initialisieren des Speedtests: {e}")
        return

    print(Fore.YELLOW + "\n🔹 Suche nach dem besten Server...")
    try:
        best_server = st.get_best_server()
        if not best_server:
            raise Exception("Kein optimaler Server gefunden.")
    except Exception as e:
        print(Fore.RED + f"❌ Fehler beim Abrufen des besten Servers: {e}")
        return

    print(Fore.YELLOW + "🔹 Starte den Speedtest... Bitte warten...")

    # Event zum Stoppen der Animation
    stop_event = threading.Event()
    loader_thread = threading.Thread(target=animated_loader, args=(stop_event,))
    loader_thread.start()

    try:
        # Durchführung des Speedtests
        download_speed = st.download() / 1_000_000  # Convert to Mbit/s
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
    except Exception as e:
        print(Fore.RED + f"❌ Fehler beim Speedtest: {e}")
        stop_event.set()
        loader_thread.join()
        return

    # Stoppe die Animation
    stop_event.set()
    loader_thread.join()

    # Ergebnisse anzeigen
    print(Fore.GREEN + f"\n🔹 Download-Geschwindigkeit: {download_speed:.2f} Mbit/s")
    print(Fore.GREEN + f"🔹 Upload-Geschwindigkeit: {upload_speed:.2f} Mbit/s")
    print(Fore.GREEN + f"🔹 Ping: {ping} ms")

    # Loggen der Ergebnisse
    log_message = f"Speedtest Ergebnisse: Download: {download_speed:.2f} Mbit/s, Upload: {upload_speed:.2f} Mbit/s, Ping: {ping} ms"
    log_to_file("speedtest", log_message)

    input(Fore.MAGENTA + "\nDrücke Enter, um fortzufahren...")