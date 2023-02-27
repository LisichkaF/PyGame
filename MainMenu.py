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

#print(pygame.font.get_fonts())

font = pygame.font.SysFont(None, 20)
menufont = pygame.font.SysFont('britannic', 20)
logoFont = pygame.font.SysFont('britannic', 70)

"""
A function that can be used to write text on our screen and buttons
"""
logo = pygame.image.load('Logo.png')
image = pygame.image.load('Button.png')
bg = pygame.image.load("bg.png")
IntroLogo = pygame.image.load("LogoPygame.png")

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later
click = False


# Main container function that holds the buttons and game functions
def intro():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(IntroLogo, (420, 254))
        pygame.mixer.music.load('IntroMusic.mp3')
        pygame.mixer.music.play(-1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)

        time.sleep(5)
        start_screen()

def start_screen():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))
        draw_text('Типа игра [нажать SPACE зайти в меню]', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load('MainMinuOst.mp3')
                    pygame.mixer.music.play(-1)
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)

def main_menu():
    global click
    while True:
        screen.fill((250, 250, 250))
        screen.blit(bg, (0, 0))
        screen.blit(logo, (200, 80))
        #draw_text('Ersalam', logoFont, (255, 193, 80), screen, 340, 80)


        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(300, 220, 320, 50)
        button_2 = pygame.Rect(300, 300, 320, 50)

        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        screen.blit(image, (button_1))
        screen.blit(image, (button_2))
        #pygame.draw.rect(screen, (19, 50, 81), button_1)
        #pygame.draw.rect(screen, (19, 50, 81), button_2)

        # writing text on top of button
        draw_text('PLAY', menufont, (255, 255, 255), screen, 450, 230)
        draw_text('OPTIONS', menufont, (255, 255, 255), screen, 430, 310)

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
    os.system("Game.py")
    pygame.quit()
    sys.exit()


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


intro()