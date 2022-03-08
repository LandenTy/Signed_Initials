"""
LESSON: 3.1 - Lines
EXERCISE: Digital Signature
"""

#### ---- SETUP ---- ####

# Import and initialize pygame
import pygame, sys
pygame.init()

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Window Initization
w = pygame.display.set_mode([500, 300])
w.fill(black)

#### ---- DRAW FUNCTIONS ---- ####

def DrawL(x, y, color):
    
    pygame.draw.line(w, color, (55 + x, 25 + y), (55 + x, 250 + y), 3)
    pygame.draw.line(w, color, (50 + x, 250 + y), (180 + x, 250 + y), 3)

def DrawB(x, y, color):
    
    pygame.draw.line(w, color, (250 + x, 25 + y), (250 + x, 250 + y), 3)
    pygame.draw.line(w, color, (250 + x, 25 + y), (280 + x, 25 + y), 3)
    pygame.draw.line(w, color, (280 + x, 25 + y), (315 + x, 45 + y), 3)
    pygame.draw.line(w, color, (315 + x, 45 + y), (335 + x, 75 + y), 3)
    pygame.draw.line(w, color, (335 + x, 75 + y), (315 + x, 115 + y), 3)
    pygame.draw.line(w, color, (315 + x, 115 + y), (250 + x, 130 + y), 3)
    pygame.draw.line(w, color, (250 + x, 130 + y), (280 + x, 145 + y), 3)
    pygame.draw.line(w, color, (280 + x, 145 + y), (315 + x, 190 + y), 3)
    pygame.draw.line(w, color, (315 + x, 190 + y), (300 + x, 215 + y), 3)
    pygame.draw.line(w, color, (300 + x, 215 + y), (250 + x, 250 + y), 3)

#### ---- DRAW LETTERS ---- ####

# First Letter
DrawL(50, 0, (255, 0, 0))

# Second Letter
DrawB(50, 0, (255, 0, 0))

#### ---- FINISH ---- ####
pygame.display.flip()

while True:
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            
            sys.exit()

# Turn in your Coding Exercise.
