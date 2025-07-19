import pygame
from pygame import gfxdraw
import random

surface=pygame.display.set_mode((400,300))
x=200
y=150
color=(255,255,255)
done=False
gfxdraw.pixel(surface,x,y,color)
i=0
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            pygame.quit()
    while i<60:
        x=x+i
        y=y+i
        i+=1
        gfxdraw.pixel(surface,x,y,color)
        pygame.display.flip()


'''

a=random.randint(1,100)'''


