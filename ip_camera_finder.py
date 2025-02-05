import ipaddress
import socket
import threading

from colorama import Fore
from nmap import nmap

from clear_screen import clear_screen


def scan_ip_for_camera_local(ip_range):
    active_cameras = []

    def check_camera(ip, port):
        try:
            # Versuche eine Verbindung zum gegebenen IP und Port
            sock = socket.create_connection((ip, port), timeout=1)
            sock.send(b"GET / HTTP/1.1\r\nHost: " + bytes(ip, 'utf-8') + b"\r\n\r\n")
            response = sock.recv(1024)

            # Hier überprüfen wir einfache HTTP-Antworten, die darauf hindeuten, dass es sich um eine Kamera handelt
            if b"camera" in response.lower() or b"stream" in response.lower():
                print(Fore.GREEN + f"Gefundene Kamera: {ip}:{port}")
                active_cameras.append(f"{ip}:{port}")
            sock.close()
        except Exception as e:
            pass  # Fehler ignorieren, wenn Verbindung nicht hergestellt werden kann

    threads = []
    for ip in ip_range:
        for port in camera_ports:
            thread = threading.Thread(target=check_camera, args=(ip, port))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    if active_cameras:
        print(Fore.CYAN + "\nGefundene IP-Kameras (Lokal):")
        for camera in active_cameras:
            print(Fore.GREEN + f"   - {camera}")
    else:
        print(Fore.RED + "Keine IP-Kameras im lokalen Netzwerk gefunden.")


def get_ip_range(local_ip, netmask):
    network = ipaddress.IPv4Network(f"{local_ip}/{netmask}", strict=False)
    return [str(ip) for ip in network.hosts()]


# Funktion, um IP-Kameras online zu suchen
def scan_ip_for_camera_online():
    # Beispielhafte Liste von bekannten IP-Bereichen oder Ziel-IPs
    known_ip_ranges = [
        "192.168.1.0/24",  # Beispiel: lokales Netzwerk
        "10.0.0.0/24"  # Beispiel: weiteres lokales Netzwerk
    ]

    nm = nmap.PortScanner()

    for cidr in known_ip_ranges:
        print(f"Scanne IP-Bereich: {cidr}")
        nm.scan(hosts=cidr, arguments='-p 80')  # Beispiel für Port-Scan auf Port 80 (HTTP)

        for host in nm.all_hosts():
            if nm[host].state() == "up":
                print(f"Host {host} ist online und läuft auf Port 80.")

        print("-" * 50)


# Funktion, um den IP Camera Finder im Menü anzubinden
def ip_camera_finder_menu():  # Neue Zeile für den Funktionskopf
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🔍 IP CAMERA FINDER".center(50))
    print(Fore.CYAN + "=" * 50)

    print(Fore.YELLOW + "Wählen Sie den Modus für die IP-Kamera-Suche:")
    print(Fore.YELLOW + "1. LAN (lokales Netzwerk)")
    print(Fore.YELLOW + "2. WAN (Online-IP-Kameras suchen)")

    mode = input(Fore.YELLOW + "Bitte wählen Sie 1 oder 2: ")

    if mode == "1":  # LAN Suche
        print(Fore.YELLOW + "\nScanne lokale IP-Adressen...")
        local_ip = socket.gethostbyname(socket.gethostname())
        ip_range = get_ip_range(local_ip, '255.255.255.0')
        scan_ip_for_camera_local(ip_range)
    elif mode == "2":  # WAN Suche
        print(Fore.YELLOW + "\nScanne online nach IP-Kameras...")
        scan_ip_for_camera_online()
    else:
        print(Fore.RED + "Ungültige Wahl. Bitte wählen Sie 1 oder 2.")

    input(Fore.MAGENTA + "\nDrücke Enter, um fortzufahren...")  # Diese Zeile am Ende
camera_ports = [80, 8080, 554, 443, 81]