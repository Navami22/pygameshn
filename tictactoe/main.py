import pygame
import random

pygame.init()
 
WIDTH,HEIGTH=300,300

window=pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("TIC TAC TOE")

def draw_window():
    clr=(255,255,255)
    lineclr=(50,50,50)
    window.fill(clr)
<<<<<<< HEAD
    for x in range(1,3):
        pygame.draw.line(window,lineclr,(0,x*100),(WIDTH,x*100))
        pygame.draw.line(window,lineclr,(x*100,0),(x*100,HEIGTH))
    pygame.display.update()
    
    
=======
    for x in range(0,3):
        pygame.draw.line(window,lineclr,(0,x*100),(width,x*100))
        pygame.draw.line(window,linecr,(x*100,0),(x*100,height))
    //pygame.display.update()
>>>>>>> 32ff933255ec52d119fe025a746985c1e0a760b7

run=True

while run:
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
pygame.quit()
            

