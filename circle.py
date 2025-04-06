import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (30, 30, 255)

screen.fill (black)
pygame.display.update()

class circle():
    def __init__(color, position, rad, width = 0):
        self.color = color
        self.position = position
        self.rad = rad
        self.width = width
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.position, self.rad, self.wid)

pos_1 = (300,300)
pos_2 = (100, 100)
pos_3 = (500, 500)
radius = 50
wid = 2

pygame.draw.circle(screen, red, pos_1, radius, wid)
pygame.draw.circle(screen, blue, pos_2, radius, wid)
pygame.draw.circle(screen, green, pos_3, radius, wid)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)