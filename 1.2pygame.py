import pygame

pygame.init()
yellow=[255,255,0]
red=[255,0,0]
green=[0,255,0]
gray=[128,128,128]
blue=[0,0,255]
brown=[139,69,19]
white=[255,255,255]
purple=[255,0,255]
black=[0,0,0]

display_size=pygame.display.set_mode((300,300))
pygame.display.set_caption("Foor - Ilja Melikov")
display_size.fill(black)
pygame.draw.rect(display_size,gray,(100,45,100,180),width=3)

pygame.draw.circle(display_size,red, (150,80),25)
pygame.draw.circle(display_size,yellow, (150,135),25)
pygame.draw.circle(display_size,green, (150,190),25)






pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()
