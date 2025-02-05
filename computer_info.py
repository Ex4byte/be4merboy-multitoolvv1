import getpass
import platform
import uuid
import socket

import psutil
import requests
from colorama import Fore


def get_system_info():
    try:
        print(Fore.CYAN + "=" * 50)
        print(Fore.CYAN + "📡 SYSTEM- & NETZWERK-INFORMATIONEN".center(50))
        print(Fore.CYAN + "=" * 50)

        # Lokale IP-Adresse
        local_ip = socket.gethostbyname(socket.gethostname())

        # Öffentliche IPv4-Adresse
        try:
            public_ip = requests.get("https://api.ipify.org", timeout=3).text
        except requests.RequestException:
            public_ip = "⚠️ Nicht verfügbar"

        # MAC-Adresse
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 48, 8)])

        # HWID (eindeutige ID der Hardware)
        hwid = str(uuid.getnode())

        # PC-Name & Benutzername
        pc_name = socket.gethostname()
        user_name = getpass.getuser()

        # Betriebssystem-Infos
        os_info = f"{platform.system()} {platform.release()} ({platform.architecture()[0]})"

        # Standard-Gateway (Router-IP)
        default_gateway = None
        for conn in psutil.net_if_addrs().values():
            for addr in conn:
                if addr.family == socket.AF_INET:
                    default_gateway = addr.address
                    break

        # RAM & CPU-Informationen
        total_ram = round(psutil.virtual_memory().total / (1024 ** 3), 2)
        cpu_cores = psutil.cpu_count(logical=True)

        # Internetverbindung prüfen
        try:
            requests.get("https://www.google.com", timeout=3)
            internet_status = Fore.GREEN + "✅ Online"
        except requests.ConnectionError:
            internet_status = Fore.RED + "❌ Keine Verbindung"

        # 📌 **Ausgabe mit Farben**
        print(Fore.YELLOW + "🖥️  SYSTEM-INFO")
        print(Fore.WHITE + f"  - PC-Name: {Fore.GREEN}{pc_name}")
        print(Fore.WHITE + f"  - Benutzername: {Fore.GREEN}{user_name}")
        print(Fore.WHITE + f"  - Betriebssystem: {Fore.GREEN}{os_info}")
        print(Fore.WHITE + f"  - HWID: {Fore.GREEN}{hwid}")

        print(Fore.YELLOW + "\n🌐 NETZWERK-INFO")
        print(Fore.WHITE + f"  - Lokale IP-Adresse: {Fore.GREEN}{local_ip}")
        print(Fore.WHITE + f"  - Öffentliche IPv4-Adresse: {Fore.GREEN}{public_ip}")
        print(Fore.WHITE + f"  - MAC-Adresse: {Fore.GREEN}{mac_address}")
        print(Fore.WHITE + f"  - Standard-Gateway: {Fore.GREEN}{default_gateway or 'Nicht gefunden'}")

        print(Fore.YELLOW + "\n⚙️  SYSTEM-LEISTUNG")
        print(Fore.WHITE + f"  - RAM: {Fore.GREEN}{total_ram} GB")
        print(Fore.WHITE + f"  - CPU-Kerne: {Fore.GREEN}{cpu_cores}")

        print(Fore.YELLOW + "\n🔗 INTERNETSTATUS")
        print(Fore.WHITE + f"  - Verbindung: {internet_status}")

        print(Fore.CYAN + "=" * 50)

    except Exception as e:
        print(Fore.RED + f"⚠️ Fehler beim Abrufen der Informationen: {e}")