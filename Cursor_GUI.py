import random
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

#Screen size constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#Target size constants
RECTANGLE_LONG_SIDE = SCREEN_HEIGHT / 4
RECTANGLE_SHORT_SIDE = RECTANGLE_LONG_SIDE / 2

#Class for the targets
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super(Target, self).__init__()
        self.surf = pygame.Surface((0,0))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
#Player is the cursor
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(
            center=(
                400,300
            )
        )

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Game loop
running = True

targets = []

#Function to define targets
#Inputs are x and y of top left, and width and height dimensions
def addTarget(x, y, width, height):
    targets.append(Target())
    targets[-1].surf = pygame.Surface((width, height))
    targets[-1].rect = targets[-1].surf.get_rect(
        topleft=(
            x, y
        )
    )

#Defining all of the targets
addTarget((SCREEN_WIDTH - RECTANGLE_LONG_SIDE * 2)/3, 0, RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE)
addTarget(SCREEN_WIDTH - (SCREEN_WIDTH - RECTANGLE_LONG_SIDE * 2)/3 - RECTANGLE_LONG_SIDE, 0, RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE)

addTarget(SCREEN_WIDTH - RECTANGLE_SHORT_SIDE, (SCREEN_HEIGHT - RECTANGLE_LONG_SIDE * 2)/3, RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE)
addTarget(SCREEN_WIDTH - RECTANGLE_SHORT_SIDE, SCREEN_HEIGHT - (SCREEN_HEIGHT - RECTANGLE_LONG_SIDE * 2)/3 - RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE)

addTarget(SCREEN_WIDTH - (SCREEN_WIDTH - RECTANGLE_LONG_SIDE * 2)/3 - RECTANGLE_LONG_SIDE, SCREEN_HEIGHT - RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE)
addTarget((SCREEN_WIDTH - RECTANGLE_LONG_SIDE * 2)/3, SCREEN_HEIGHT - RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE)

addTarget(0, SCREEN_HEIGHT - (SCREEN_HEIGHT - RECTANGLE_LONG_SIDE * 2)/3 - RECTANGLE_LONG_SIDE, RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE)
addTarget(0, (SCREEN_HEIGHT - RECTANGLE_LONG_SIDE * 2)/3, RECTANGLE_SHORT_SIDE, RECTANGLE_LONG_SIDE)

# Move the sprite based on user keypresses
#Currently the horizontal and vertical parameters are set to zero, but these go into the 'self.rect.move_ip()'
def update(self, horizontal=0, vertical=0):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)
    # self.rect.move_ip(horizontal, vertical)

 # Keep player on the screen
    if self.rect.left < 0:
        self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT

#Function to random spawn a target
def playScreen():
    target = random.randint(0,7)
    return targets[target]
    
#Function to make target flash after the cursor reaches it
def flashing(target):
    black = (0,0,0)
    grey = (100,100,100)
    for i in range(2):
        target_displayed.surf.fill(grey)
        screen.blit(target_displayed.surf, target_displayed.rect)
        pygame.display.update(target_displayed)
        pygame.time.delay(250)
        target_displayed.surf.fill(black)
        screen.blit(target_displayed.surf, target_displayed.rect)
        pygame.display.update(target_displayed)
        pygame.time.delay(250)

player = Player()
player.surf = pygame.Surface((0,0))
target_displayed = Target()

#Function to play the game and display stuff
def game():
    screen.fill((255,255,255))
    pygame.display.flip()
    pygame.time.delay(1000)
    target_displayed = playScreen()
    screen.blit(target_displayed.surf, target_displayed.rect)
    pygame.display.update(target_displayed)
    pygame.time.delay(1000)
    player = Player()

#Creating events for GUI
PLAYGAME = pygame.USEREVENT + 0
pygame.time.set_timer(PLAYGAME, 10000)

screen.fill((255,255,255))
pygame.display.flip()
pygame.time.delay(1000)
target_displayed = playScreen()
screen.blit(target_displayed.surf, target_displayed.rect)
pygame.display.update(target_displayed)
pygame.time.delay(1000)
player = Player()

#Make the game slower
clock = pygame.time.Clock()

while running:

    screen.fill((255,255,255))

    #Checks for events   
    for event in pygame.event.get():

        #Checks for keydown
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
        
        if event.type == PLAYGAME:
            game()
            
            
            
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    
    # Update the player sprite based on user keypresses
    update(player, pressed_keys)
 
    
    

    
    
    if pygame.sprite.collide_rect(player, target_displayed):
        pygame.time.set_timer(PLAYGAME, 0)
        flashing(target_displayed)
        screen.fill((255,255,255))
        player.surf = pygame.Surface((0,0))
        pygame.display.flip()
        pygame.time.delay(1000)
        
        target_displayed = playScreen()
        screen.blit(target_displayed.surf, target_displayed.rect)
        pygame.display.update(target_displayed)

        pygame.time.delay(1000)
        player = Player()
        pygame.time.set_timer(PLAYGAME, 10000)


    screen.blit(player.surf, player.rect)
    screen.blit(target_displayed.surf, target_displayed.rect)

    pygame.display.flip()
    clock.tick(60)
    
