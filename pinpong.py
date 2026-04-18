from random import *
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y <win_height-100:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y <win_height-100:
            self.rect.y += self.speed
class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
font.init()
font1 = font.Font(None,36)
mixer.init()
window = display.set_mode((700,500))
win_width = 700
win_height = 500
speed1 = 10
x1 = 50
y1= 250
speed_y = 6
speed2 = 6
display.set_caption('Пинпонг')
player1=Player("player.png",x1,y1,speed1,40,100)
player2=Player("player.png",(x1+570),y1,speed1,40,100)
ball = Bullet("ball.png",350,250,speed2,40,40)
background = transform.scale(image.load('galaxy.jpg'),(700,500))
clock = time.Clock()
FPS = 60
total = 0
text_lose = font1.render('you all lose',True,(255,255,55))
finish = False
game = True
while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    if finish!=True:
        window.blit(background,(0,0))
        ball.reset()
        player1.reset()
        player1.update1()
        player2.reset()
        player2.update2()
        ball.rect.x += speed2
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y*= -1
        sprites_list1 = sprite.collide_rect(player1,ball)
        sprites_list2 = sprite.collide_rect(player2,ball)
        if sprites_list2 or sprites_list1:
            speed2 *= -1
        if ball.rect.x > 680 or ball.rect.x < 20:
            total += 1
            ball.rect.x = 350
            ball.rect.y = 250
        if total == 3:
            window.blit(text_lose,(200,200))
            finish = True
    display.update()
    clock.tick(FPS)
