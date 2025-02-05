# 🔍 CFX Lookup (Cyan für Infos, Rot für Fehler)
import requests
from colorama import Fore
from clear_screen import clear_screen


def cfx_lookup():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🔍 CFX-LOOKUP".center(50))
    print(Fore.CYAN + "=" * 50)

    cfx_code = input(Fore.YELLOW + "\n🔹 Gib den CFX Code ein: ")
    request = f"https://cfx.re/join/{cfx_code}" if not cfx_code.startswith("https://") else cfx_code

    try:
        response = requests.get(request)
        ip_address = response.headers.get("x-citizenfx-url", "Nicht verfügbar").replace("http://", "").replace("/", "")
        print(Fore.CYAN + f"\n🔹 Server IP: {ip_address}")
    except requests.exceptions.RequestException:
        print(Fore.RED + "❌ Fehler! Server offline oder ungültiger Code.")
    except Exception as e:
        print(Fore.RED + f"❌ Fehler: {e}")


# 🌎 IP Lookup (Cyan für Details, Gelb für Eingaben, Rot für Fehler)
