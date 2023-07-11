from pygame import *
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60


def generate_color():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT - 150:
            self.rect.y += self.speed

racket_1 = Player('racket.png', 30, 200, 50, 150, 4)
racket_2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

speeed_x = 3
speeed_y = 3

background = generate_color()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-Pong')
clock = time.Clock()

font.init()
font1 = font.Font(None, 36)
lose1 = font1.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font1.render("PLAYER 2 LOSE!", True, (180, 0, 0))

color_selecting = False
finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            color_selecting = True
        elif e.type == MOUSEBUTTONUP and e.button == 1:
            color_selecting = False
        

    if not finish:
        if color_selecting:
            background = generate_color()
        window.fill(background)
        racket_1.update_l()
        racket_2.update_r()
        ball.rect.x += speeed_x
        ball.rect.y += speeed_y
        racket_1.reset()
        racket_2.reset()
        ball.reset()

        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speeed_x *= -1
            speeed_y *= 1

        if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
            speeed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200, 200))
        
        if ball.rect.x > WIDTH:
            finish = True
            window.blit(lose2, (200, 200))


    display.update()
    clock.tick(FPS)