import pygame


class InputBox:
    def __init__(self, x, y, w, h, font, inactive_color, active_color, text_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = inactive_color # grey
        self.color_active = active_color # blue
        self.color = self.color_inactive
        self.text_color = text_color # black
        self.font = font
        self.text = ""
        self.int_value = None
        self.txt_surface = self.font.render(self.text, True, self.text_color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state on click
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                # if event.key == pygame.K_RETURN:
                
                if event.unicode:
                    if event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]  # Remove last character
                    else:
                        self.text += event.unicode

                try:
                    self.int_value = str(self.text)
                    print(f"Integer input: {self.int_value}")  # Do something with the integer
                except ValueError:
                    print("Invalid input! Please enter an integer.")

                # Re-render text
                self.txt_surface = self.font.render(self.text, True, self.text_color)


        return self.int_value

    def draw(self, surface):
        # Draw text
        surface.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw the input box rectangle
        pygame.draw.rect(surface, self.color, self.rect, 2)

    def update(self):
        # Adjust the width of the input box based on the text
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width