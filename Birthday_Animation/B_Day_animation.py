import pygame
import time

pygame.init()
WIDTH = 600
HEIGHT = 600

black = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

image1 = pygame.image.load("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/backgroundone.jpg").convert()
image = pygame.transform.scale(image1, (WIDTH, HEIGHT))

while (True):
    font = pygame.font.SysFont("Times New Roman", 72)
    text1 = font.render("Happy", True, (0, 0, 0))
    text2 = font.render("Bithday", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    screen.blit(text1, (210, 180))
    screen.blit(text2, (180, 264))
    pygame.display.update()
    time.sleep(2)

    image2 = pygame.image.load("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/backgroundtwo.jpg")
    font2 = pygame.font.SysFont("Arial", 36)
    text3 = font2.render("Wishing You a Bright Future Ahead", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(image2, (0, 0))
    screen.blit(text3, (30, 30))
    pygame.display.update()
    time.sleep(2)

    image3 = pygame.image.load("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/backgroundthree.jpg")
    screen.fill((255, 255, 255))
    screen.blit(image3, (0, 0))
    pygame.display.update()
    time.sleep(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)





