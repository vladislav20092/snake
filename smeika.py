import pygame
import random

w , h = 1000, 600
screen = pygame.display.set_mode((w,h))
fps = pygame.time.Clock()
size = 40

class GameObject:
    def __init__(self,x,y,color):
        self.hitbox = pygame.Rect(x,y,size,size)
        self.image = pygame.Surface((size,size))
        self.image.fill(color)
x = size * random.randrange(w/size -1)
y = size * random.randrange(h/size -1)
food = GameObject (x,y,(100,0,100))

class Snake(GameObject):
    speedx = size
    speedy = 0
    timer = 0
    def move(self):
        if self.timer == 0:
            self.hitbox.x += self.speedx
            self.hitbox.y += self.speedy
            self.timer = 25
        self.timer -= 1
    def control(self):
        k_list = pygame.key.get_pressed()
        if k_list [pygame.K_w]:
            self.speedx = 0
            self.speedy = -size
        if k_list [pygame.K_d]:
            self.speedx = 0
            self.speedy = size
        if k_list [pygame.K_h]:
            self.speedx = 0
            self.speedy = size
        if k_list [pygame.K_w]:
            self.speedx = 0
            self.speedy = -size
snake = Snake(0,0,(0,225,0))


     



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit (food.image,food.hitbox)
    screen.blit (snake.image,snake.hitbox)
    snake.move()
    snake.control()
    pygame.display.update()
    fps.tick(60)