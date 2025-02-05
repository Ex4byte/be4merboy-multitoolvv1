
import os
from clear_screen import clear_screen
from tracer import traceroute
from colorama import init
from port_scan import port_scan
from cfx_lookup import cfx_lookup
from ip_lookup import ip_lookup
from ping_tool import ping_host
from computer_info import get_system_info
from dns_resolve import dns_reverse_lookup
from ip_camera_finder import ip_camera_finder_menu
from speedtest_runner import run_speedtest
# Initialize Colorama
init(autoreset=True)

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Define color codes
dark_red = "\033[31m"  # Red for box outlines
dark_purple = "\033[35m"  # Purple for option text
cyan = "\033[36m"  # Cyan for the numbers and brackets
light_blue = "\033[94m"  # Light blue for aesthetic number and brackets
reset_color = "\033[0m"  # Reset color

# ASCII Logos (fixed logo)

# ASCII Logo (with colors intact)
box_width = 46

# ASCII Logo (without color reset issues)
ascii_fixed_logo = [
    "    ⠀⠀⣠⡶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀",
    "⢸⣿⣯⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀",
    "⢼⣿⣿⣆⠀⢀⣀⣀⣴⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀",
    "⢸⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⢻⣿⠋⠙⢿⣿⣿⡀⠀⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⢸⠿⢆⣀⣼⣿⣿⣿⣿⡏⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⡀⣨⡙⠟⣩⣙⣡⣬⣴⣤⠏⠀⠀⠀⠀⠀⠀⣀⡀",
    "⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⣀⣤⣾⣿⣿⡇",
    "⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣇⠀⢸⣿⣿⠿⠿⠛⠃",
    "⠀⠀⠀⠀⢠⣿⣿⢹⣿⢹⣿⣿⣿⢰⣿⠿⠃⠀⠀⠀⠀",
    "⠀⢀⣀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡛⠀⠀⠀⠀⠀⠀",
    "⠀⠻⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠛⠓⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀"
]


def print_header():
    """ Center ASCII above the left-aligned header while keeping it red """
    max_ascii_width = max(len(line) for line in ascii_fixed_logo)  # Get ASCII width
    ascii_padding = max(0, (box_width - max_ascii_width) // 2)  # Center relative to header

    # Print ASCII, ensuring each line starts with dark_red
    for line in ascii_fixed_logo:
        print(f"{dark_red}{' ' * ascii_padding}{line}{reset_color}")

    # Header directly below, left-aligned
    header = f"""{dark_red}
╔{"═" * (box_width - 1)}╗
║  Willkommen im Multitool{" " * (box_width - 26)}║
╚{"═" * (box_width - 1)}╝
{reset_color}"""
    print(header)



# 🎛 Hauptmenü
def print_menu():
    # Fixed width of the menu box
    box_width = 46

    # Define the box around the menu options with all outlines in dark red
    box_top = "╔" + "═" * (box_width - 1) + "╗"
    box_bottom = "╚" + "═" * (box_width - 1) + "╝"

    menu_options = [
        "[1] Computer Info",
        "[2] Ping",
        "[3] Traceroute",
        "[4] Port-Scan",
        "[5] CFX Lookup",
        "[6] IP Lookup",
        "[7] DNS Lookup",
        "[8] Speedtest",
        "[9] IP Camera Finder",
        "[0] Beenden",
    ]

    # Print left-aligned menu (no padding)
    print(dark_red + box_top + reset_color)
    for option in menu_options:
        index, text = option.split("] ", 1)
        line = f"{dark_red}║ {light_blue}{index}]{dark_purple} {text:<{box_width - len(index) - 4}}{dark_red}║{reset_color}"
        print(line)
    print(dark_red + box_bottom + reset_color)



def main_menu():
    while True:
        print(dark_purple + "🌐 be4merboy Network Multitool 🌐\n" + reset_color)
        print_header()  # Print the header above the menu options
        print_menu()  # Call the function for printing the menu

        choice = input(dark_purple + "\n👉 Wählen Sie eine Option: " + reset_color)

        if choice == "1":
            get_system_info()
        elif choice == "2":
            ping_host()
        elif choice == "3":
            traceroute()
        elif choice == "4":
            port_scan()
        elif choice == "5":
            cfx_lookup()
        elif choice == "6":
            ip_lookup()
        elif choice == "7":
            dns_reverse_lookup()
        elif choice == "8":
            run_speedtest()
        elif choice == "9":
            ip_camera_finder_menu()
        elif choice == "0":
            print(dark_red + "Beende das Programm..." + reset_color)
            os._exit(0)
        else:
            print(dark_red + "Ungültige Auswahl." + reset_color)

        input(dark_purple + "\n🔄 Drücken Sie Enter, um fortzufahren..." + reset_color)
        clear_screen()

def main():
    """Startet das Programm."""
    #play_music()
    main_menu()  # Menü im Hauptthread

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")  # Show the large ASCII splash
    main()


