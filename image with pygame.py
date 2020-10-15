import pygame
pygame.init()

display_surface = pygame.display.set_mode((500,450))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            quit()
    pygame.draw.rect(display_surface,(0,125,255),pygame.Rect(30,30,60,60))
    pygame.display.flip()
