import json

import requests
from colorama import Fore, Style

from clear_screen import clear_screen


def ip_lookup():
    clear_screen()
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "🔍 IP-LOOKUP".center(50))
    print(Fore.CYAN + "=" * 50)

    ip = input(Fore.YELLOW + "\n🔹 Gib die IP-Adresse ein: " + Fore.WHITE)
    print(Fore.CYAN + f"\n🔍 Suche nach Details für IP {ip}...\n")

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()

        # Extracting values with fallback to "Unbekannt"
        city = data.get('city', 'Unbekannt')
        region = data.get('region', 'Unbekannt')
        country = data.get('country', 'Unbekannt')
        org = data.get('org', 'Unbekannt')
        timezone = data.get('timezone', 'Unbekannt')
        postal = data.get('postal', 'Unbekannt')
        coordinates = data.get('loc', 'Unbekannt')

        print(Fore.GREEN + f"🔹 Details für {ip}:")
        print(Fore.CYAN + f"   🏙 Stadt: {city}")
        print(Fore.CYAN + f"   📍 Region: {region}")
        print(Fore.CYAN + f"   🌎 Land: {country}")
        print(Fore.CYAN + f"   🏢 Organisation: {org}")
        print(Fore.CYAN + f"   ⏰ Zeitzone: {timezone}")
        print(Fore.CYAN + f"   📌 Koordinaten: {coordinates}")
        print(Fore.CYAN + f"   📨 Postleitzahl: {postal}")

        if coordinates != 'Unbekannt':
            lat_lon = coordinates.replace(" ", "")  # Entfernen von Leerzeichen
            maps_url = f"https://www.google.com/maps/search/?api=1&query={lat_lon}"
            print(Fore.BLUE + f"   🔗 Google Maps: {maps_url}")
        else:
            print(Fore.RED + "❌ Keine Koordinaten verfügbar – Google Maps-Link nicht möglich.")

    except requests.exceptions.RequestException:
        print(Fore.RED + "❌ Netzwerkfehler! Überprüfe deine Internetverbindung.")
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Fehlerhafte Antwort vom Server.")
    except ValueError:
        print(Fore.RED + "❌ Fehler beim Verarbeiten der Koordinaten.")

    print(Style.RESET_ALL)  # Reset color formatting
