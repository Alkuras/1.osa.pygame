from random import randint
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
def cloud():
    x=randint(100,600) 
    y=randint(50,300)
    
    pygame.draw.circle(display_size,gray, (x,y),50)
    pygame.draw.circle(display_size,gray, (x+30,y+30),40)
def flower():
    p=0
    for i in range(20):
        pygame.draw.circle(display_size,purple, (300,200),5+p,width=2)
        pygame.draw.circle(display_size,yellow, (300,200),4+p,width=1)
        pygame.draw.circle(display_size,red, (300,200),3+p,width=1)
        p+=5
    pygame.draw.line(display_size,green,(300,300),(300,500),10)
def bee():
    x=randint(100,600) 
    y=randint(50,300)
    bee=pygame.image.load("bee.png")
    bee=pygame.transform.scale(bee,(100,100))
    display_size.blit(bee,(x,y))

    


pygame.init()
yellow=[255,255,0]
red=[255,0,0]
green=[0,255,0]
darkgreen=[0,100,0]
gray=[128,128,128]
blue=[0,0,255]
brown=[139,69,19]
white=[255,255,255]
purple=[255,0,255]

display_size=pygame.display.set_mode((800,600))
pygame.display.set_caption("Flower")
display_size.fill(white)
pygame.draw.rect(display_size,red,(100,100,200,100))
pygame.draw.rect(display_size,green, (0, 400, 800, 400))
pygame.draw.rect(display_size,blue, (0, 0, 800, 400))

pygame.draw.circle(display_size,yellow, (30,30),50)
sun()
cloud()
cloud()
flower()
bee()
bee()
grass()



font=pygame.font.SysFont("Arial",50)
message="Welcome"
add_text=font.render(message,True,red)
display_size.blit(add_text,(400,500))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()
