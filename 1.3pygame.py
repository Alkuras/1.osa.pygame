import pygame
def sun():
    x=200
    y=0
    for i in range(10):
        
        x-=20   
        y+=20
        if i in range(3,7):
            pygame.draw.line(display_size,yellow,(0,0),(x+i,y+i),5)
        else:
            pygame.draw.line(display_size,yellow,(0,0),(x,y),5)
pygame.init()
yellow=[255,255,0]
red=[255,0,0]
green=[0,255,0]
gray=[100,100,100]
blue=[0,0,255]
brown=[139,69,19]

display_size=pygame.display.set_mode((640,480))
pygame.display.set_caption("Zoinks")
bg_image = pygame.image.load('place.jpg')
bg_image=pygame.transform.scale(bg_image,(640,480))
display_size.blit(bg_image,(0,0))


shag=pygame.image.load("shaggy.png")
shag=pygame.transform.scale(shag,(200,200))
display_size.blit(shag,(300,250))

vill=pygame.image.load("villian.png")
vill=pygame.transform.scale(vill,(200,200))
display_size.blit(vill,(50,200))

font=pygame.font.SysFont("Arial",20,bold=True)
message="Zoinks!"
add_text=font.render(message,True,green,gray)
display_size.blit(add_text,(500,270))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()
