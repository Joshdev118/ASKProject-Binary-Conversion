import pygame
from Dropdown import Dropdown
from Textbox import InputBox
from Resultbox import OutputBox
from Converter import Converter


pygame.init()


screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Binary Conversion')


WIN_C = (29, 29, 27)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SELECT = (33, 33, 30)

font = pygame.font.Font("Font/Pixel.ttf", 13)
font_s = pygame.font.Font("Font/Pixel.ttf", 11)
font_b = pygame.font.Font("Font/Pixel.ttf", 20)

dropdown = Dropdown(120, 70, 200, 40, font, BLUE, GRAY, BLUE, BLACK, SELECT, ["Decimal", "Octal", "Hexadecimal", "Binary"])
                                # mainbox, optionbox, maintext, optiontext, selectcolor 
dropdown2 = Dropdown(550, 70, 200, 40, font, BLUE, GRAY, BLUE, BLACK, SELECT, ["Decimal", "Octal", "Hexadecimal", "Binary"])

input_box = InputBox(120, 280, 140, 32, font, GRAY, BLUE, BLACK)

output_box = OutputBox(550, 280, 140, 32, font, BLACK, GRAY)

converter = Converter()

bg = pygame.image.load("Image/backdrop.png")   # background
bg.set_alpha(6)
text1 = font_s.render("_Josh_118_", False, GRAY) # _Josh_118_
text1.set_alpha(100)
arrow = font_b.render(">", False, WHITE)  # arrow >
arrow.set_alpha(50)


clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WIN_C)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        type1 = dropdown.handle_event(event)
        type2 = dropdown2.handle_event(event)

        input = input_box.handle_event(event)

    input_box.update()
    input_box.draw(screen)

    dropdown.draw(screen)
    dropdown2.draw(screen)
    output_box.update(screen, converter.update(type1, type2, input))

    screen.blit(bg, (0, 0))
    screen.blit(text1, (780, 480))
    screen.blit(arrow, (430, 78))

    print (type1, type2, input)
    pygame.display.update()

    clock.tick(70)

pygame.quit()