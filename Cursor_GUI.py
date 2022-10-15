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

#Class for the targets
class Target(pygame.sprite.Sprite):
    def __init__(self):
        super(Target, self).__init__()
        self.surf = pygame.Surface((0,0))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect()

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
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

#defining targets and sizes
targets = []
for i in range(8):
    targets.append(Target())
    if i == 0 or i == 1 or i == 4 or i == 5:
        targets[i].surf = pygame.Surface((200,75))
    else:
        targets[i].surf = pygame.Surface((75,200))

#Defining positions of all targets
#I'm sure there's a more efficient way of doing this but I don't know it right now

#Target 1
targets[0].rect = targets[0].surf.get_rect(
    midtop=(
        233,0
    )
)

#Target 2
targets[1].rect = targets[1].surf.get_rect(
    midtop=(
        800 - 233,0
    )
)

#Target 3
targets[2].rect = targets[2].surf.get_rect(
    midright=(
        800, 166
    )
)

#Target 4
targets[3].rect = targets[3].surf.get_rect(
    midright=(
        800,600 - 166
    )
)

#Target 5
targets[4].rect = targets[4].surf.get_rect(
    midbottom=(
        800 - 233,600
    )
)

#Target 6
targets[5].rect = targets[5].surf.get_rect(
    midbottom=(
        233,600
    )
)

#Target 7
targets[6].rect = targets[6].surf.get_rect(
    midleft=(
        0,600 - 166
    )
)

#Target 8
targets[7].rect = targets[7].surf.get_rect(
    midleft=(
        0,166
    )
)

# Move the sprite based on user keypresses
#Below are the indices correlating to the keys in the pressed_keys array
#K_UP = 82
#K_DOWN = 81
#K_LEFT = 80
#K_RIGHT = 79
def update(self, horizontal=0, vertical=0):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
        #print('up')
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
        #print('down')
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
        #print('left')
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)
        #print('right')

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


#Creating events for GUI
PLAYGAME = pygame.USEREVENT + 0
pygame.time.set_timer(PLAYGAME, 10000)

screen.fill((255,255,255))
pygame.display.flip()
pygame.time.delay(1000)
target_displayed = targets[random.randint(0,7)]
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
            screen.fill((255,255,255))
            pygame.display.flip()
            pygame.time.delay(1000)
            target_displayed = playScreen()
            screen.blit(target_displayed.surf, target_displayed.rect)
            pygame.display.update(target_displayed)
            
            pygame.time.delay(1000)
            player = Player()
            
            
            
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
    
