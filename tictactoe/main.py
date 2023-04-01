import pygame
import random

pygame.init()
 
WIDTH,HEIGTH=300,300

window=pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("TIC TAC TOE")
icon = pygame.image.load("tic-tac-toe.png")
pygame.display.set_icon(icon)
x=pygame.image.load("x.png")
o=pygame.image.load("o.png")

def draw_window():
    clr=(0,0,0)
    lineclr=(255,255,255)
    window.fill(clr)
    for x in range(1,3):
        pygame.draw.line(window,lineclr,(0,x*100),(WIDTH,x*100))
        pygame.draw.line(window,lineclr,(x*100,0),(x*100,HEIGTH))
    pygame.display.update()
    
    

run=True

while run:
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    
pygame.quit()
            

