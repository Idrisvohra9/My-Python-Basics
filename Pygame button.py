import pygame as pg
from playsound import playsound
pg.init()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
HEIGHT, WIDTH = 480, 640
SURFACE = pg.display.set_mode((WIDTH,HEIGHT))
# FPS=60
display_surface = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.SysFont('Verdana', 26)

run= True
clock = pg.time.Clock()
SURFACE.fill(WHITE)
keys= pg.key.get_pressed()

class button:
    def __init__(self, x, y,width, height,text_color,rect_color,radius, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color= text_color
        self.rect_color = rect_color
        self.radius = radius

    def text_display(self):
        text = font.render(str(self.text), True, self.text_color)
        display_surface.blit(text, (self.x, self.y))

		
    def Draw(self, win):
        pg.draw.rect(win,self.rect_color,(self.x*5/7, self.y*5/7, self.width, self.height),border_radius=self.radius)

b1= button(250, 220,160,120,BLACK,RED,2,"Resume")
b1.Draw(display_surface)

b1.text_display()

pg.display.update()
while run:
	# clock.tick(FPS) # This means that the game will run at 60 FPS
    pg.display.set_caption("Button")
    pg.display.update()
    for event in pg.event.get():
    	if event.type == pg.QUIT:
            run= False
            pg.quit()

    # if keys[pg.K_f]:
    #     # pg.display.toggle_fullscreen()
    #     playsound('D:\\Python work progress\\Python easy projects\\coins-handling.wav')