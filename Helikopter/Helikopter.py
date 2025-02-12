#!/usr/bin/env python

import pygame  
from pygame._sdl2 import Window, Texture, Image, Renderer
import math
import random

import intro_alex
import sound_alex
import engine_alex

TITLE = "Helikopter" 
FPS = 60 

screen_size_x=1900
screen_size_y=800
game_mode=0 #intro

def main(winstyle=0):
      
    pygame.display.init()
    heli_image=intro_alex.IntroImage("heliport.png" ,screen_size_x,screen_size_y)
    icon=pygame.transform.scale(heli_image.image, (32, 32))   

    win = Window(TITLE, (screen_size_x,screen_size_y), resizable=False)
    win.set_icon(icon)
    #win.set_fullscreen(True)
    renderer = Renderer(win)
    
    
    sound_alex.mixer_init()
    sound_alex.sound_heli_play()
    #sound_alex.muzic_play()
    engine_alex.engine_init(renderer,screen_size_x,screen_size_y)

    renderer.clear()    
    clock = pygame.time.Clock()

    game_mode=0  # 0 - 1 - 2
    intro_alex.intro_init(screen_size_x,screen_size_y)
    intro=intro_alex.Intro(renderer, screen_size_x,screen_size_y)

        
    run=1
    try:
        while run==1:

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                                            #mouse
                                            continue
                    if event.type == pygame.KEYDOWN:
                                if game_mode==2:
                                                    engine_alex.set_key(event.key)
                                if game_mode==1:                                                    
                                                    game_mode=2

                    if event.type == pygame.KEYUP:
                                if game_mode==2:
                                                    engine_alex.clear_key(event.key)

                    if event.type == pygame.QUIT:
                                                pygame.quit()
                                                run=0
                                                break
                renderer.draw_color=(0,0,0,0)
                renderer.clear()
                if game_mode==0:
                            #------intro------
                            intro.update()
                            intro.draw()
                            if intro.curr_action==3:
                                            game_mode=1
                                            sound_alex.sound_heli_stop()
                                            sound_alex.muzic_play()
                if game_mode==1:
                            intro.update()
                            intro.draw()             
                                    
                            #------intro------
                if game_mode==2:
                            #------GAME------
                            engine_alex.engine()                            
                            #------GAME------



                renderer.present()                                
                clock.tick(FPS)
                win.title = str("FPS: {}".format(clock.get_fps()))
              

    finally:
        pygame.quit()


# call the "main" function if running this script
main()
