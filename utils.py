
import pygame
import os


def load_sprite(name, with_alpha=True):
    # Corrected path to match assets/sprites/ directory
    path = os.path.join("assets", "sprites", f"{name}.png")
    print(f"[DEBUG] Looking for image at: {path}")  # Print image path for debugging

    loaded_sprite = pygame.image.load(path)
    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


def print_text(surface, text, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    rect.center = (surface.get_width() // 2, surface.get_height() // 2)
    surface.blit(text_surface, rect)
