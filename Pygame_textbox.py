import pygame
pygame.init()
x, y = 640, 480
WIN=pygame.display.set_mode((x,y))
Black_shade=(23,19,20)
White = (255,255,255)
Blue =(0,0,255)
FPS= 20
WIN.fill(Black_shade)
# pygame.draw.rect(WIN, Blue, (10,10,2,20),1)
def Blinker(x,y):
    pygame.draw.rect(WIN, Blue, (x,y,2,20),1)

def main():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        WIN.fill(Black_shade)
        Blinker(10,10)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            # elif pygame.
if __name__ == "__main__":    
    main()