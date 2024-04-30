#! C:\Users\Mayeu\OneDrive\Desktop\BPM\venv\Scripts\python.exe
import pygame
import time
import sys

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

font = pygame.font.Font(None, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
tempo = input("Enter tempo please\n")
beat_duration = int(60 * 1000 / int(tempo))
pygame.mixer.music.load("venv/HH Neat.adv.ogg")
# Initialize boolean values
metro_on: bool = False
playing: bool = True

# Initialize how many milliseconds their has been since pygame was initialized
next_beat_time = pygame.time.get_ticks()  # Get the current time
beats: list = []
taps: list = []
clock = pygame.time.Clock()

while playing:
    tapped = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("P key pressed")
                metro_on = True
                next_beat_time = pygame.time.get_ticks() + beat_duration  # Schedule the first beat
            elif event.key == pygame.K_s:
                print("S key pressed")
                metro_on = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                tempo = int(tempo) - 1
                beat_duration = int(60 * 1000 / int(tempo))
                print(tempo)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                tempo = int(tempo) + 1
                beat_duration = int(60 * 1000 / int(tempo))
                print(tempo)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if metro_on:

                    taps.append(pygame.time.get_ticks())
                    tapped = True
            elif event.type != pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if metro_on:

                    taps.append(0)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            
                    
    
    current_time = pygame.time.get_ticks()  # Get the current time
    if metro_on and current_time >= next_beat_time:
        pygame.mixer.music.play(), beats.append(pygame.time.get_ticks())  # Play the metronome sound
        print(pygame.time.get_ticks())
        
        next_beat_time += beat_duration  # Schedule the next beat
        if not tapped:
            taps.append(0)
    pygame.display.update()
    clock.tick_busy_loop(beat_duration)
    

print(len(beats))
print(len(taps))
print(beats)
print(taps)
"""if len(beats) > len(taps):
    beats = beats[:len(taps)]"""
accuracy: list = [beats[x] - taps[x] for x in range(len(beats))]
pygame.quit()
