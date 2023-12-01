from typing import Any
import pygame
import time
import random
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, QUIT, KEYDOWN, K_a, K_s, K_w, K_d
)

# These will come in handy!
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

# Player 1 uses up and down arrow keys
class Player1(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player1, self).__init__()
        self.surf = pygame.Surface((25,100))          # Input an (x, y) tuple to give it a width and height
        self.surf.fill((255, 0, 0))       # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        self.rect.x = 150
        self.rect.y = 250
        # Right now, Player1 spawns in at (0,0). Set the x and y values of self.rect to some other numbers to change this
    # Updates this player's position
    def update(self, keys):
        if keys[K_w]:
            if(self.rect.y > 0):
                self.rect.move_ip(0,-9)
        if keys[K_s]:
            if(self.rect.y < 500):
                self.rect.move_ip(0,9)


# Player2 uses W and S keys
class Player2(Player1):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((25,100))          # Input an (x, y) tuple to give it a width and height
        self.surf.fill((0, 0, 255)) # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        self.rect.x = 750
        self.rect.y = 250
    # Updates this player's position
    def update(self, keys):
        if keys[K_UP]:
            if(self.rect.y > 0):
                self.rect.move_ip(0,-9)
        if keys[K_DOWN]:
            if(self.rect.y < 500):
                self.rect.move_ip(0,9)


directions = [-1,1]
ballspeeds = [3, -3]
score = [0,0]
scoreincrease = 1

#ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill([255,255,255])
        self.rect = self.surf.get_rect()
        self.rect.x =  450
        self.rect.y = 250
        self.movementx = random.choice(ballspeeds)
        self.movementy = random.choice(ballspeeds)

#changes the balls position, speed, and scores list
    def update(self) -> None:
        if(self.rect.y > 0 and self.rect.y < 590):
        
            self.rect.x += self.movementx
            self.rect.y += self.movementy

        #if player two wins
        elif (self.rect.x < 11):
            score[1] += scoreincrease
            self.rect.x = 450
            self.rect.y = 250
            self.movementx = random.choice(ballspeeds)
            self.surf.fill((255,255,255))

        #if player one wins
        elif(self.rect.x > 889):
            score[0] += scoreincrease
            self.rect.x = 450
            self.rect.y = 250
            self.movementx = random.choice(ballspeeds)
            self.surf.fill((255,255,255))
        else:
            #changes direction fo the ball
            self.movementy = self.movementy * -1
            self.rect.x += self.movementx
            self.rect.y += self.movementy

            

        

clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # (x, y)

# Create objects for player1, player2, and the ball here
ball = Ball()
david = Player1()
bryce = Player2()
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
all_sprites.add(david)
all_sprites.add(bryce)

# Add those objects to all_sprites and/or players, respectively

running = True
while running:
    clock.tick(80)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Update positions
    pressed_keys = pygame.key.get_pressed()
    david.update(pressed_keys)

    pressed_keys = pygame.key.get_pressed()
    bryce.update(pressed_keys)

    for player in players:
        player.update(pressed_keys)
    # Call update() on the ball here
    ball.update()
    if pygame.sprite.spritecollideany(ball, all_sprites):
        ball.movementx *= -1
        if ball.movementx > 0:
            ball.movementx += 1
        else:
            ball.movementx -= 1
        
        ball.movementy *= random.choice(directions)
        if pygame.sprite.collide_rect(ball, david):
            ball.surf.fill((255,0,0))
        else: 
            ball.surf.fill((0,0,255))


    # Render
    screen.fill((0, 0, 0))
    # Use blit() to draw each sprite on the screen here
    pygame.init()
    screen.blit(david.surf, david.rect)
    screen.blit(bryce.surf, bryce.rect)
    screen.blit(ball.surf, ball.rect)
    # Gives our text font as well as initizes 
    font = pygame.font.Font("arial.ttf", 32)
    score_text = font.render(f'Score: {score[0]} to {score[1]}', True, (255, 255, 255))
    screen.blit(score_text, (350, 10))
    pygame.display.flip()
    
