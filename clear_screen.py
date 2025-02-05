# Funktion um den Bildschirm zu löschen
import os
import platform


def clear_screen():
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')