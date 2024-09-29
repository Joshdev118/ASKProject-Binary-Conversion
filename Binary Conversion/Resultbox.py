import pygame
from Converter import Converter

class OutputBox:
    def __init__(self, x, y, w, h, font, text_color, box_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.text_color = text_color
        self.color = box_color
        self.text = str()
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.converter = Converter()


    def update(self, surface, value):
        # Adjust the width of the input box based on the text
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

        print(self.text) 
        self.text = value

        # Re-render text
        self.txt_surface = self.font.render(self.text, True, self.text_color)

        # Draw text
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw the input box rectangle
        pygame.draw.rect(surface, self.color, self.rect, 2)
