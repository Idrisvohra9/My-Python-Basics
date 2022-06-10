import pygame
pygame.init()

size = (400, 250)
screen = pygame.display.set_mode(size)
GOLD=(255,215,0)
WHITE=(255,255,255)
BLACK=(0,5,0)

screen.fill(WHITE)
pygame.display.update()
dead=True

clock = pygame.time.Clock()
PI=3.14

while(dead):
    for i in range(0,1000,10):
    
        pygame.draw.arc(screen, GOLD, [80-i,10,250,200], PI/2, PI, 5)
        # pygame.draw.arc(screen, GOLD, [80,10,250,200], 0, PI/2, 2)
        pygame.draw.arc(screen, GOLD, [80+i,10,250,200], PI*2, 2*PI, 5)
        # pygame.draw.arc(screen, GOLD, [80,10,250,200], PI, 3*PI/2, 2)
        clock.tick(10)
        # screen.fill(BLACK)

        pygame.display.update()
        pygame.display.flip()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            dead = False

    # pygame.draw.rect(screen, GOLD, [80,10,250,200], 2)
    
   
#Shutdown display module