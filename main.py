from pygame import *
from random import randint


class Ball():
    
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
 
       
        self.image = transform.scale(image.load(player_image).convert_alpha(), (w, h))
        self.speed = player_speed
 
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Ball):

    def update(self):
        self.reload += 1
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("ping-pong")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player1 = Player('rocket1.png', -300, 0, 4, 65, 65)


