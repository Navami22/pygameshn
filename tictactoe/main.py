import pygame
import random

pygame.init()
 
WIDTH,HEIGTH=400,400

WIN=pygame.display.set_mode(WIDTH,HEIGTH)
pygame.display.set_caption("TIC TAC TOE")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()
            

