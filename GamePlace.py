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
animation_set = [pygame.image.load(f"{i}Transition.png") for i in range(1, 11)]

image = pygame.image.load('LitleButton.png')
But = pygame.image.load('Button.png')
UlanBG = pygame.image.load('Ulanbator.png')
UlanBG = pygame.transform.scale(UlanBG, (960, 600))
DiaScreen = pygame.image.load('Dialog screen.png')
DiaScreen = pygame.transform.scale(DiaScreen, (960, 600))
Batiy = pygame.image.load('Char1.png')
Batiy = pygame.transform.scale(Batiy, (600, 600))
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
    global i
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
        screen.blit(UlanBG, (0, 0))
        draw_text('Типа игра [нажать SPACE зайти в меню]', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    UlaanbaatorDialog()

        pygame.display.update()
        mainClock.tick(60)

def UlaanbaatorDialog():
    lives = "Hi"
    global click
    while True:
        screen.fill((250, 250, 250))
        screen.blit(UlanBG, (0, 0))
        screen.blit(DiaScreen, (0, 0))

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(700, 380, 320, 50)
        button_2 = pygame.Rect(700, 460, 320, 50)
        #button_3 = pygame.Rect(700, 540, 320, 50)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                UlaanbaatorSecondDialog()
                lives += "Good luck"
        if button_2.collidepoint((mx, my)):
            if click:
                main_menu()
                lives += "Okey"
        #if button_3.collidepoint((mx, my)):
            #if click:
                #lives += "Goodbye"
        screen.blit(But, (button_1))
        screen.blit(But, (button_2))
        #screen.blit(But, (button_3))

        text = font.render(str(lives), True, (200, 200, 200))
        screen.blit(text, (600, 100))
        # pygame.draw.rect(screen, (19, 50, 81), button_1)
        # pygame.draw.rect(screen, (19, 50, 81), button_2)

        # writing text on top of button
        draw_text('1. Прогулятся по городу', font, (255, 255, 255), screen, 730, 390)
        draw_text('2. Покинуть город', font, (255, 255, 255), screen, 730, 470)
        #draw_text('3.', font, (255, 255, 255), screen, 730, 550)

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

def UlaanbaatorSecondDialog():
    lives = "Вскоре вы встретили мужчины одетого в ватник и малгай." \
            "*Что ты здесь делаешь республиканец?* недовольно произносит он"
    global click
    while True:
        screen.fill((250, 250, 250))
        screen.blit(UlanBG, (0, 0))
        screen.blit(DiaScreen, (0, 0))
        screen.blit(Batiy, (10, 10))

        mx, my = pygame.mouse.get_pos()

        # creating buttons
        button_1 = pygame.Rect(700, 380, 320, 50)
        button_2 = pygame.Rect(700, 460, 320, 50)
        button_3 = pygame.Rect(700, 540, 320, 50)
        # defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                lives += "Не будь так груб я за *Хана*"
        if button_2.collidepoint((mx, my)):
            if click:
                main_menu()
                lives += "Okey"
        if button_3.collidepoint((mx, my)):
            if click:
                lives += "Goodbye"
        screen.blit(But, (button_1))
        screen.blit(But, (button_2))
        screen.blit(But, (button_3))

        text = font.render(str(lives), True, (200, 200, 200))
        screen.blit(text, (600, 100))
        # pygame.draw.rect(screen, (19, 50, 81), button_1)
        # pygame.draw.rect(screen, (19, 50, 81), button_2)

        # writing text on top of button
        draw_text('1. Не будь так груб я за *Хана*', font, (255, 255, 255), screen, 730, 390)
        draw_text('2. Покинуть город', font, (255, 255, 255), screen, 730, 470)
        draw_text('3.', font, (255, 255, 255), screen, 730, 550)

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