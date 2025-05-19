
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
grey=[128,128,128]
blue=[0,0,255]
brown=[139,69,19]

display_size=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame window")
display_size.fill(grey)
pygame.draw.rect(display_size,red,(100,100,200,100))

pygame.draw.circle(display_size,yellow, (30,30),50)
sun()

pygame.draw.polygon(display_size,blue,[(600,100),(700,100),(650,50)])
pygame.draw.line(display_size,yellow,(100,500),(700,500),5)
image1=pygame.image.load("catdog.png")
image1=pygame.transform.scale(image1,(100,100))
display_size.blit(image1,(300,400))

font=pygame.font.SysFont("Arial",50)
message="Welcome"
add_text=font.render(message,True,red)
display_size.blit(add_text,(400,500))

pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
pygame.quit()