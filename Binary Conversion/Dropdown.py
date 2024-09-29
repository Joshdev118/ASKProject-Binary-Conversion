import pygame

class Dropdown:
    def __init__(self, x, y, w, h, font, main_color, option_color, main_text_color, option_text_color, selected_color, options):
        self.rect = pygame.Rect(x, y, w, h)  # main button box
        self.font = font
        self.main_color = main_color
        self.option_color = option_color
        self.main_text_color = main_text_color
        self.option_text_color = option_text_color
        self.selected_color = selected_color

        self.options = options
        self.active_option = None  
        self.is_open = False 
        self.options_rects = [pygame.Rect(x + 25, y + h * (i + 1), w - 50, h) for i in range(len(options))] # option box

    def draw(self, surface):
        # Draw the main button
        pygame.draw.rect(surface, self.main_color, self.rect, 3, 50)
        text = self.font.render(self.options[self.active_option] if self.active_option is not None else "Select", True, self.main_text_color)
        surface.blit(text, text.get_rect(center=self.rect.center))

        # Draw the options when dropdown is open
        if self.is_open:
            for i, option_rect in enumerate(self.options_rects):
            

                if option_rect.collidepoint(pygame.mouse.get_pos()):  # changes color of option once hover
                    pygame.draw.rect(surface, self.selected_color, option_rect)
                    option_text = self.font.render(self.options[i], True, self.option_text_color)

                else:
                    pygame.draw.rect(surface, self.option_color, option_rect)
                    option_text = self.font.render(self.options[i], True, self.option_text_color)

                surface.blit(option_text, option_text.get_rect(center=option_rect.center))


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if self.rect.collidepoint(event.pos):
                # Toggle dropdown open/close
                self.is_open = not self.is_open

            elif self.is_open:
                # Check if clicked on any option
                for i, option_rect in enumerate(self.options_rects):
                    if option_rect.collidepoint(event.pos):
                        self.active_option = i
                        self.is_open = False
                        break
                    
        return self.active_option

