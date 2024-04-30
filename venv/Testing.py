#! C:\Users\Mayeu\OneDrive\Desktop\BPM\venv\Scripts\python.exe
import pygame
import time
import sys



pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tempo = input("Enter tempo please\n")

beat_duration = int(60 * 1000 / int(tempo))
beat_duration /= 1000
pygame.mixer.music.load("venv/HH Neat.adv.ogg")

metro_on = False
playing = True
while playing:
    
    for event in pygame.event.get():
    
        if metro_on:
            time.sleep(beat_duration)
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.pause()
        if event.type == pygame.QUIT:
            playing = False
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space key pressed")
                metro_on = True  # Start the loop
            elif event.key == pygame.K_s:
                print("S key pressed")
                metro_on = False  # Exit the loop
    
        
       
                

pygame.quit()
sys.exit()
        