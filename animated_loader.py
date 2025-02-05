import sys
import time

from colorama import Fore, Style


def animated_loader(event):
    """Zeigt eine Ladeanimation an, bis das Event gesetzt wird."""
    animation = ['|', '/', '-', '\\']
    idx = 0
    while not event.is_set():
        sys.stdout.write(f"\r{Fore.YELLOW}🔹 Messen der Geschwindigkeit {animation[idx]} {Style.RESET_ALL}")
        sys.stdout.flush()
        idx = (idx + 1) % len(animation)
        time.sleep(0.2)
    sys.stdout.write("\r" + " " * 50 + "\r")  # Löscht die Animation