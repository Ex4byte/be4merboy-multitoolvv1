import socket
from colorama import Fore
from clear_screen import clear_screen


def dns_reverse_lookup():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🔍 DNS & REVERSE DNS-LOOKUP".center(50))
    print(Fore.CYAN + "=" * 50)

    user_input = input(Fore.YELLOW + "\n🔹 Gib eine IP-Adresse oder einen Domainnamen ein: ")

    try:
        # Überprüfen, ob es sich um eine IP-Adresse oder einen Domainnamen handelt
        socket.inet_aton(user_input)  # Wenn es eine gültige IP-Adresse ist
        print(Fore.CYAN + f"\n🔹 Reverse DNS Lookup für IP {user_input}...")

        try:
            domain_name = socket.gethostbyaddr(user_input)[0]
            print(Fore.GREEN + f"🔹 Der Domainname für {user_input} ist: {domain_name}")
        except socket.herror:
            print(Fore.RED + "❌ Fehler: Kein Domainname für diese IP-Adresse gefunden.")

    except socket.error:
        print(Fore.CYAN + f"\n🔹 DNS Lookup für Domain {user_input}...")

        try:
            ip_address = socket.gethostbyname(user_input)
            print(Fore.GREEN + f"🔹 Die IP-Adresse für {user_input} ist: {ip_address}")
        except socket.gaierror:
            print(Fore.RED + "❌ Fehler: Die Domain konnte nicht aufgelöst werden.")
