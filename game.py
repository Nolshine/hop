import pygame
from pygame.locals import *

pygame.init()


#global constants here
GAME_RES = (800, 600)

class Player:
    colour = (50, 255, 80, 1)
    shadow = (0, 0, 0, 0.2)

    def __init__(self, x, z):
        print "initializing player."

        self.size = 6
        self.x = x
        self.y = 0
        self.z = z
        self.xvel = 0.0
        self.yvel = 0.0
        self.zvel = 0.0
        self.topvel = ((-1)*GAME_RES[0]/100, GAME_RES[0]/100,
                       (-1)*GAME_RES[1]/100, GAME_RES[1]/100)

    def update(self, keys):
##        print "checking for key events."
        if self.y > 0:
            self.yvel -= 0.2
        if self.y <= 0:
            self.y = 0
            self.yvel = 0
        if keys != []:
            if K_COMMA in keys and (not self.xvel <= self.topvel[0]):
                self.zvel -= 0.2
            if K_o in keys and (not self.xvel >= self.topvel[1]):
                self.zvel += 0.2
            if K_a in keys and (not self.xvel <= self.topvel[2]):
                self.xvel -= 0.2
            if K_e in keys  and (not self.xvel >= self.topvel[3]):
                self.xvel += 0.2
            if self.y == 0 and (K_SPACE in keys):
                self.yvel = 3
                
##        print "adding velocities to position."
        self.x += self.xvel
        self.y += self.yvel
        self.z += self.zvel

    def draw_self(self, screen):
        x = int(round(self.x)+self.size)
        z = int(round(self.z)+self.size)
        y = int(round(self.y))
        rect = pygame.Rect(0, 0, self.size*1.8, self.size)
        rect.left = self.x
        rect.bottom = int(round(self.z))+(self.size*2)
        pygame.draw.ellipse(screen, Player.shadow, rect)
        pygame.draw.circle(screen, Player.colour,
                           (x, z-y), self.size)

def main():
    print "initializing display and clock."
    screen = pygame.display.set_mode(GAME_RES, DOUBLEBUF)
    
    clock = pygame.time.Clock()
    running = True

    keys = []
    player = Player(GAME_RES[0]/2, GAME_RES[1]/2)

    while running:
        clock.tick(35)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                keys.append(event.key)
            if event.type == KEYUP:
                keys.remove(event.key)

        pygame.display.set_caption(str(player.y))

        player.update(keys)
        
        screen.fill((90,90,90, 1))
        player.draw_self(screen)
        pygame.display.update()

        


main()
pygame.quit()
print "successful quit."
        
            
