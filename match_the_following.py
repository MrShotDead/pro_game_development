import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))
pygame.display.update()

subway_surfer = pygame.image.load ("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/subway_surfers.png")
ludo = pygame.image.load ("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/ludo.png")
temple_run = pygame.image.load ("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/temple_run.png")
candy_crush = pygame.image.load ("C:/Users/win/Desktop/JetLearn/Pro_Game_Development/Images/candy_crush.png")

screen.blit(subway_surfer, (150, 100))
screen.blit(ludo, (150, 200))
screen.blit(temple_run, (150, 300))
screen.blit(candy_crush, (150, 400))

font = pygame.font.SysFont("Time New Roman", 36)

text_1 = font.render("Ludo", True, (0, 0, 0))
text_2 = font.render("Sunbway Surfers", True, (0, 0, 0))
text_3 = font.render("Candy Crush", True, (0, 0, 0))
text_4 = font.render("Temple Run", True, (0, 0, 0))

screen.blit(text_1, (350, 100))
screen.blit(text_2, (350, 200))
screen.blit(text_3, (350, 300))
screen.blit(text_4, (350, 400))

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 0, 0), (pos), 20, 0)
        pygame.display.update()

    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0), (pos), (pos2),5)
        pygame.draw.circle(screen, (0,0,0) ,(pos2), 20, 0)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()

pygame.quit()