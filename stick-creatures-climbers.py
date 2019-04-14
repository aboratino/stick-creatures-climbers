# ===================================
# Stick Creatures - Climbers
#   Anthony Boratino 2013-2019
#
#   Simulate evolution of climbing by stick creatures
#   Each creature consists of an array of segments.
#   The head and tail are represented by green dots
#   that act as suction cups to attain locomotion.
#   When they are glowing they are activated.
#
#   Every so often the creatures all breed with whichever
#   one is closest to the top.
# ===================================

import pygame.gfxdraw

from creature import Creature

# Setup screen
width = 1024
height = 768
SIZE = (width, height)
title = "Stick Creatures - Climbers"

# Startup
pygame.init()
pygame.display.set_caption(title)
screen = pygame.display.set_mode(SIZE)
done = False

# Simulation variables
population = 25                 # number of creatures to spawn
creatures = []                  # empty array of creatures
n_steps = 0                     # simulation step
n_gens = 0                      # number of generations
BREED_INTERVAL = 2000           # breeding interval
BEST_H_RESET = 2000             # impossible number for height reset
best_height = BEST_H_RESET      # Current best height
best = 0                        # index of best creature

# create creatures
for i in range(population):
    creatures.append(Creature(i, screen))

# Main loop

while not done:

    n_steps += 1
    screen.fill((0, 0, 0))

    # Breeding
    if n_steps % BREED_INTERVAL == 0:
        n_gens += 1
        best_height = BEST_H_RESET
        creatures[best].is_stud = False
        best = 0

        # Creature wins if it is both inbounds on left and right of screen,
        # and has climbed the farthest.
        for i in range(len(creatures)):
            if creatures[i].get_loc()[1] < best_height and\
                    0 < creatures[i].get_loc()[0] < width:
                best_height = creatures[i].get_loc()[1]
                best = i
        creatures[best].is_stud = True

        print "Generation:", n_gens, " Best: #", best, "Height:", best_height
        for i in range(len(creatures)):
            creatures[i].reset_location()
            if i != best:
                creatures[i].breedwith(creatures[best])

    # Update and draw creature
    for i in range(len(creatures)):
        creatures[i].update()
        creatures[i].draw()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                done = True

    pygame.display.flip()
pygame.quit()

