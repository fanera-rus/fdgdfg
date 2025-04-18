from pygame import *

from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image , (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height ):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.speed = 2
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >=win_width - 85:
            self.direction = 'left'

        if self.direction =='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 700-65:
            self.rect.x += 4
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 4
        if keys_pressed[K_s] and self.rect.y < 500-65 :
            self.rect.y += 4
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 4


win_width = 700
win_height = 500

player = Player('hero.png', 5, win_height-80, 4)
monster = Enemy('cyborg.png',  win_width-80, 280, 2)
tresuare = GameSprite('treasure.png',  win_width-120, win_height-80, 0)

c1 = randint(0, 255)
c2 = randint(0, 255)
c3 = randint(0, 255)

w1 = Wall(c1, c2, c3, 100, 20, 450, 10)
w2 = Wall(c1, c2, c3, 100, 480, 390, 10)
w3 = Wall(c1, c2, c3, 100, 20, 10, 380)
w4 = Wall(c1, c2, c3, 400, 100, 10, 380)
w5 = Wall(c1, c2, c3, 300, 20, 10, 380)
w6 = Wall(c1, c2, c3, 200, 100, 10, 380)
w7 = Wall(c1, c2, c3, 500, 20, 10, 380)

window = display.set_mode((win_width, win_height)) 
display.set_caption('Maze')

background = transform.scale(image.load('background.jpg'), (win_width, win_height))

game = True
clock = time.Clock()
FPS = 60

'''mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()'''

finish = False
font.init()
font = font.Font(None, 70)
win = font.render('Ура, победа!', True,(255, 215, 0))
lose = font.render('Увы, проигрыш!', True,(255, 215, 0))
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            game = False
    if finish:
        player.rect.x, player.rect.y = 5, win_height - 80
        finish = False
    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
        finish = True
        window.blit(lose, (200, 200))
    if sprite.collide_rect(player, tresuare):
        finish = False
        window.blit(win, (200, 200))
    
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    
    player.reset()
    monster.reset()
    tresuare.reset()
    monster.update()
    player.update()
    display.update()
    clock.tick(FPS)