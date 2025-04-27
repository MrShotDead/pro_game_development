import pygame
from pygame.locals import *
import time
import random

pygame.init()
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
player_x = 200
player_y = 200

keys = [False, False, False, False]
player = pygame.image.load("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/ship.jpg")
bg = pygame.image.load("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/space.jpg")

while player_y < 600:
    screen.blit(bg, (0, 0))
    screen.blit(player, (player_x,  player_y))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        #check if any keyboard button is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        
        #check if any keyboard button is released
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False

    #adding movement
    if keys[0]:
        if player_y > 0:
            player_y -= 7

    if keys[2]:
        if player_y < 536:
            player_y +=7

    if keys[1]:
        if player_x > 0:
            player_x -= 2
    
    if keys[3]:
        if player_x < 536:
            player_x += 2

    player_y += 5
    time.sleep(0.05)

print("Game Over")