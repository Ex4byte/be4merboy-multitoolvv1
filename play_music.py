import pygame


def play_music():
    """Startet die Hintergrundmusik."""
    pygame.mixer.init()
    pygame.mixer.music.load("background.mp3")  # Replace with your file
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(1)