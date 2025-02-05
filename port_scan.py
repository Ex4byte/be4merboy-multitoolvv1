import socket
import threading

from colorama import Fore

from clear_screen import clear_screen


def port_scan():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🔍 PORT-SCAN".center(50))
    print(Fore.CYAN + "=" * 50)

    target = input(Fore.YELLOW + "\n🔹 Geben Sie die Ziel-IP-Adresse oder den Hostnamen ein: ")

    try:
        target_ip = socket.gethostbyname(target)
        print(Fore.GREEN + f"Ziel-Host aufgelöst: {target_ip}")

        start_port = int(input(Fore.YELLOW + "🔹 Start-Port: "))
        end_port = int(input(Fore.YELLOW + "🔹 End-Port: "))

        open_ports = []

        def scan_port(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                if s.connect_ex((target_ip, port)) == 0:
                    open_ports.append(port)
                    print(Fore.GREEN + f"Port {port} ist offen.")
                else:
                    print(Fore.RED + f"Port {port} ist geschlossen.")

        threads = [threading.Thread(target=scan_port, args=(p,)) for p in range(start_port, end_port + 1)]
        for t in threads: t.start()
        for t in threads: t.join()

        if open_ports:
            print(Fore.GREEN + f"\n🔹 Offene Ports: {', '.join(map(str, open_ports))}")
        else:
            print(Fore.RED + "❌ Keine offenen Ports gefunden.")

    except Exception as e:
        print(Fore.RED + f"❌ Fehler: {e}")