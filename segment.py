# Stick Creatures - Climbers
#  defines segments
#  ~ Anthony Boratino 2013-2019

import pygame
import pygame.gfxdraw

# Some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FULL_GREEN = (0, 255, 0)
DULL_GREEN = (0, 128, 0)

# Segment Constants
SWING_COUNTER = 400
SEGMENT_LENGTH = 15

# circle sizes
SIZE_JOINT = 1
SIZE_HEAD = 5
SIZE_WINNER = 7
SIZE_TAIL = 4


# class Segment
#
# defines a single segment
#
class Segment:
    def __init__(self, screen):
        self.screen = screen
        self.length = SEGMENT_LENGTH    # segment length
        self.bx = 0                     # begin x
        self.by = 0                     # begin y
        self.ex = 0                     # end x
        self.ey = 0                     # end y
        self.grotation = 0              # segments genetic start rotation
        self.rotation = 0               # segments current rotation
        self.rot_rate = 0               # rate of rotation
        self.sforward = True            # swinging segment forward or bak
        self.counter = 0                # swing counter
        self.color_a = FULL_GREEN       # active color and inactive colors
        self.color_b = DULL_GREEN       # inactive color
        self.is_stud = False            # Winner?
        self.is_first = False
        self.is_last = False

    # swap colors for 'suction cups' and
    # reverse direction of swing
    def reverse_swing(self):
        self.color_a, self.color_b = self.color_b, self.color_a
        self.sforward = not self.sforward

    def update(self):
        # if swinging forward # else swinging back
        if self.sforward:
            self.rotation += self.rot_rate
        else:
            self.rotation -= self.rot_rate

        # increment swing timer and check if it's time to reverse
        self.counter += 1
        if self.counter >= SWING_COUNTER:
            self.reverse_swing()
            self.counter = 0

    def draw(self):
        # draw lines to represent segments
        pygame.gfxdraw.line(self.screen,
                            self.bx,
                            self.by,
                            self.ex,
                            self.ey,
                            WHITE)

        # draw a joint between segments
        if not self.is_first and not self.is_last:
            pygame.gfxdraw.filled_circle(self.screen,
                                         self.bx,
                                         self.by,
                                         SIZE_JOINT,
                                         BLUE)

        # if first point
        if self.is_first:
            # draw the 'head'
            pygame.gfxdraw.filled_circle(self.screen,
                                         self.bx,
                                         self.by,
                                         SIZE_HEAD,
                                         self.color_a)

            # draw a red circle around the head if creature is a winner.
            if self.is_stud:
                self.is_stud = False
                pygame.gfxdraw.aacircle(self.screen,
                                        self.bx,
                                        self.by,
                                        SIZE_WINNER,
                                        RED)

        # if last point
        if self.is_last:
            pygame.gfxdraw.filled_circle(self.screen,
                                         self.ex,
                                         self.ey,
                                         SIZE_TAIL,
                                         self.color_b)
