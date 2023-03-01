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
image = pygame.image.load('LitleButton.png')
bg = pygame.image.load("HrenMap.png")
RealBG = pygame.transform.scale(bg, (960, 600))



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# A variable to check for the status later
click = False


# Main container function that holds the buttons and game functions
def main_menu():
    quit = False
    global click
    while True:
        screen.fill((250, 250, 250))
        screen.blit(RealBG, (0, 0))
        #draw_text('Ersalam', logoFont, (255, 193, 80), screen, 340, 80)


        mx, my = pygame.mouse.get_pos()

        # creating buttons
        Novoudinsk = pygame.Rect(900, 120, 320, 50)
        Ulaanbaator = pygame.Rect(880, 175, 320, 50)
        Dihua = pygame.Rect(640, 250, 320, 50)
        Alat = pygame.Rect(500, 275, 320, 50)
        Kabul = pygame.Rect(425, 410, 320, 50)
        Tegran = pygame.Rect(220, 380, 320, 50)
        Ersalam = pygame.Rect(30, 450, 320, 50)


        # defining functions when a certain button is pressed
        if Novoudinsk.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                game()
        if Ulaanbaator.collidepoint((mx, my)):
            if click:
                UlaanbaatorTown()
        if Dihua.collidepoint((mx, my)):
            if click:
                DihuaTown()
        if Alat.collidepoint((mx, my)):
            if click:
                AlatTown()
        if Kabul.collidepoint((mx, my)):
            if click:
                KabulTown()
        if Tegran.collidepoint((mx, my)):
            if click:
                TegranTown()
        if Ersalam.collidepoint((mx, my)):
            if click:
                ErsalamTown()
        screen.blit(image, (Novoudinsk))
        screen.blit(image, (Ulaanbaator))
        screen.blit(image, (Dihua))
        screen.blit(image, (Alat))
        screen.blit(image, (Kabul))
        screen.blit(image, (Tegran))
        screen.blit(image, (Ersalam))

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

def UlaanbaatorTown():
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

def DihuaTown():
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

def AlatTown():
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

def KabulTown():
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

def TegranTown():
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

def ErsalamTown():
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
main_menu()