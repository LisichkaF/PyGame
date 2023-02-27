'''
import os
import pygame
import sys
import time
"""
Setting up an envisys.exit() ronment to initialize pygame
"""
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((960, 599), 0, 32)
TownDict =  {'Novoudin': 120, 'Ulaanbaator': 230, 'Dihua': 345, 'Alat': 450, 'Kabul': 560, 'Tegran': 670, 'Ersalam': 700}
#первая цифра означает личный номер, вторая и третья пути, если третья 0 значит путь всего один. Если и второе и третье это 0 то конец игры
#print(pygame.font.get_fonts())

font = pygame.font.SysFont(None, 20)
menufont = pygame.font.SysFont('britannic', 20)
logoFont = pygame.font.SysFont('britannic', 70)
"""
A function that can be used to write text on our screen and buttons
"""
image = pygame.image.load('Button.png')
bg = pygame.image.load("bg.png")


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later
click = False


# Main container function that holds the buttons and game functions
def main():
    cityCode = 1
    print(TownDict.get())
    lives = "Hi"
    global click
    while True:
        screen.fill((250, 250, 250))
        screen.blit(bg, (0, 0))


        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(600, 380, 320, 50)
        button_2 = pygame.Rect(600, 460, 320, 50)
        button_3 = pygame.Rect(600, 540, 320, 50)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                lives = "Good luck"
        if button_2.collidepoint((mx, my)):
            if click:
                lives = "Okey"
        if button_3.collidepoint((mx, my)):
            if click:
                lives = "Goodbye"
        screen.blit(image, (button_1))
        screen.blit(image, (button_2))
        screen.blit(image, (button_3))

        text = font.render(str(lives), True, (200, 200, 200))
        screen.blit(text, (600, 100))
        #pygame.draw.rect(screen, (19, 50, 81), button_1)
        #pygame.draw.rect(screen, (19, 50, 81), button_2)

        # writing text on top of button
        draw_text('1.', menufont, (255, 255, 255), screen, 630, 390)
        draw_text('2.', menufont, (255, 255, 255), screen, 630, 470)
        draw_text('3.', menufont, (255, 255, 255), screen, 630, 550)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


"""
This function is called when the "PLAY" button is clicked.
"""


def game():
    pass


"""
This function is called when the "OPTIONS" button is clicked.
"""


def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        draw_text('Типа настройки [нажать ESC чтобы вернутся в меню]', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main()
'''