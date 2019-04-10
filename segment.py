# defines creature segments
# each segment is an element of a linked list

import pygame
import pygame.gfxdraw

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

SWING_TIME = 250


class Segment:
    def __init__(self, screen):
        self.screen = screen
        self.prv = 0                    # previous segment
        self.nxt = 0                    # next segment
        self.nxt_bx = 0
        self.nxt_by = 0
        self.prv_ex = 0
        self.prv_ey = 0
        self.length = 12                # segment length
        self.bx = 0                     # begin x
        self.by = 0                     # begin y
        self.ex = 0                     # end x
        self.ey = 0                     # end y
        self.grotation = 0              # segments genenetic start rotation
        self.rotation = 0               # segments current rotation
        self.rot_rate = 0               # rate of rotation
        self.sforward = True            # swinging segment forward or bak
        self.counter = 0                # swing counter
        self.a_color = (0, 255, 0)      # active color
        self.i_color = (0, 128, 0)      # inactive color
        self.is_special = False         # Winner?
        self.is_first = False
        self.is_last = False

    def reverse_swing(self):
        self.a_color, self.i_color = self.i_color, self.a_color
        self.sforward = not self.sforward
        self.counter = 0

    def update(self):
        # if swinging forward # else swinging back
        if self.sforward:
            self.rotation += self.rot_rate
        else:
            self.rotation -= self.rot_rate

        # increment swing timer and check if it's time to reverse
        self.counter += 1
        if self.counter >= SWING_TIME:
            self.reverse_swing()

    def draw(self):
        pygame.gfxdraw.line(self.screen, int(self.bx), int(self.by), int(self.ex), int(self.ey), WHITE)

        if not self.is_first and not self.is_last:
            pygame.gfxdraw.aacircle(self.screen, int(self.bx), int(self.by), 3, BLUE)
        # if first point
        if self.is_first:
            pygame.gfxdraw.filled_circle(self.screen, int(self.bx), int(self.by), 5, self.a_color)
            # draw a white circle around the head if creature is a stud.
            if self.is_special:
                self.is_special = False
                pygame.gfxdraw.aacircle(self.screen, int(self.bx), int(self.by), 7, (255, 255, 255))

        # if last point
        if self.is_last:
            pygame.gfxdraw.filled_circle(self.screen, int(self.ex), int(self.ey), 4, self.i_color)
