import pygame
import random

pygame.init()
 
WIDTH,HEIGTH=300,300

window=pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("TIC TAC TOE")

def draw_window()
    clr=(244,244,244)
    lineclr=(50,50,50)
    window.fill(clr)
    for x in range(0,3):
        pygame.draw.line(window,lineclr,(0,x*100),(width,x*100))
        pygame.draw.line(window,linecr,(x*100,0),(x*100,height))
    pygame.display.update()

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()
            

