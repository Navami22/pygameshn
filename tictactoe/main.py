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

markers=[]
pos=[]

def draw_window():
    clr=(0,0,0)
    lineclr=(255,255,255)
    window.fill(clr)
    for x in range(1,3):
        pygame.draw.line(window,lineclr,(0,x*100),(WIDTH,x*100))
        pygame.draw.line(window,lineclr,(x*100,0),(x*100,HEIGTH))
    pygame.display.update()
    
for x in range(3):
    row=[0]*3
    markers.append(row)

print(markers)

run=True

while run:
    draw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
            		cell_x=pos[0]
            		cell_y=pos[1]
    
pygame.quit()
            

