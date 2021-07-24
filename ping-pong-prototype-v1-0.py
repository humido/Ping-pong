from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):#SUPER IMPORTANT
       #Call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)
 
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#main player class
class Player(GameSprite):
   #method to control the sprite with arrow keys
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #method to "shoot" (use the player position to create a bullet there)
   def fire(self):
        if len(bullets) < 6:
            bullet = Bullet(img_bullet, ship.rect.x+30, win_height-20, 20,20,10)
            bullets.add(bullet)
            fire_sound.play()

class Ball(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width-80)
            self.rect.y = 0

#images used
img_back = "background.jpg"
img_ball = "ball.png"
img_racket = "racket.png"




#Create a window
win_width = 700
win_height = 500
display.set_caption("Ping-pong game (prototype)")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

ball = Ball(img_ball, 5, win_height - 100, 80, 100, 10)
paddle1 = Player(img_racket, 20, 300, 30, 100, 10)
paddle2 = Player(img_racket, win_width - 60, 300, 30, 100, 10)



run = True #the flag is reset by the window close button
while run:

    #update the background
    window.blit(background,(0,0))


    paddle1.update()
    paddle2.update()
    ball.update()

    paddle1.reset()
    paddle2.reset()
    ball.reset()



    display.update()

    #the loop is executed each 0.05 sec
    time.delay(50)