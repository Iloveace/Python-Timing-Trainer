#! C:\Users\Mayeu\OneDrive\Desktop\BPM\venv\Scripts\python.exe
from math import comb
import pygame
import time
import sys

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400





class in_mill():
    """This class is designed to calculate the data from the metronome application by
    taking two lists. One list is the beats measured in milliseconds from when the program
    begins and the second list is the users taps that are measured in milliseconds from
    when the program begins..."""

    def __init__(self, data_beats: list, data_taps: list):
        
        self.data_beats = data_beats
        self.data_taps = data_taps
        
    
    def calculate(self)-> None:
        """In the case when the metronome stops on a beat and the users beat does not have
        the oppurtunity to be recorded, we add a 0 at the end of the list for easier comparison..."""

        if len(self.data_beats) > len(self.data_taps):
            self.data_taps.append(0)
        return
    
    def get_accurate_data(self)-> list:

        comb: list = [beats[x] - taps[x] for x in range(len(beats))]
        
        accurate: list = [x for x in comb if x < 500 and x > -500]

        return accurate
        


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
tapped: bool = True

while playing:
  
    # Event queue
    for event in pygame.event.get():
        # if you press the x then the window closes
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
            elif event.key == pygame.K_LEFT:
                tempo = int(tempo) - 1
                beat_duration = int(60 * 1000 / int(tempo))
                print(tempo)
            elif event.key == pygame.K_RIGHT:
                tempo = int(tempo) + 1
                beat_duration = int(60 * 1000 / int(tempo))
                print(tempo)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if metro_on:

                    taps.append(pygame.time.get_ticks())
                    tapped = True
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            
           
        
            
        
    current_time = pygame.time.get_ticks()  # Get the current time
    if metro_on and current_time >= next_beat_time :
        pygame.mixer.music.play(), beats.append(pygame.time.get_ticks())  # Play the metronome sound
        print(pygame.time.get_ticks())
        
        next_beat_time += beat_duration  # Schedule the next beat
        if not tapped:
            taps.append(0)
        tapped = False
    pygame.display.update()
    clock.tick_busy_loop(beat_duration)
    
    


"""if len(beats) > len(taps):
    taps.append(0)"""
"""print(len(beats))
print(len(taps))
print(beats)
print(taps)"""

"""accuracy: list = [beats[x] - taps[x] for x in range(len(beats))]
print(f"Timing accuracy in milliseconds {accuracy}")
accurate: list = [x for x in accuracy if x < 500 and x > -500]
print(accurate)"""

data = in_mill(beats, taps)
print(data.get_accurate_data())
pygame.quit()
