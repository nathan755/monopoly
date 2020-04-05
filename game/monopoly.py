import pygame
import os
from game_objects import MonopolyProperty
pygame.init()
window = pygame.display.set_mode((1000,1000))
board_img = pygame.image.load(os.path.join("assets","board2.jpg"))
# test = MonopolyProperty(3,787,130,80,2,"roverway",100)
# test2=  MonopolyProperty(3,622,130,80,2,"merciard",100)
#cord = pygame.mouse.get_pos()

def main_game_loop():
    while True:
       
       
        #cord = pygame.mouse.get_pos()
        #print(cord)
        
        window.blit(board_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()


    
    
    
    
    
