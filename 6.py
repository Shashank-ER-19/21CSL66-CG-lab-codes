import pygame,random
pygame.init()
screen=pygame.display.set_mode((800,600))
# pygame.display.set_caption("Animations")
white=(255,255,255)
colors=[(255,0,0),(0,255,0),(0,0,255)]
object=[{'x':random.randint(50,750),
         'y':random.randint(50,550),
         'radius':random.randint(10,30),
         'color':random.choice(colors),
         'speed_x':random.randint(-5,5),
         'speed_y':random.randint(-5,5)}
        for _ in range(10)]
running,clock=True,pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill(white)
    for obj in object:
        obj["x"]+=obj["speed_x"]
        obj["y"]+=obj["speed_y"]
        if obj["x"]-obj["radius"]<0 or obj["x"]+obj["radius"]>800:
            obj["speed_x"]=-obj["speed_x"]
        if obj["y"]-obj["radius"]<0 or obj["y"]+obj["radius"]>600:
            obj["speed_y"]=-obj["speed_y"]
        pygame.draw.circle(screen,obj["color"],(obj["x"],obj["y"]),obj["radius"])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()