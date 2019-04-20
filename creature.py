# Stick Creatures - Climbers
# defines creature
#   ~ Anthony Boratino 2013-2019

from segment import Segment
from random import randrange, random
import math


RESET_Y = 600           # Y location of creature upon reset_location()
RESET_X_OFFSET = 150    # How far out to push creatures from left side of screen
RESET_X_MUL = 30        # how far out to place creature, RESET_X_MUL * cid
CHANCE = 12             # 1 in CHANCE chance of mutation.
N_SEGMENTS = 8          # number of segments per creature


# Creature class
class Creature:
    def __init__(self, cid, screen):
        self.cid = cid                  # creature id
        self.screen = screen
        self.n_segments = N_SEGMENTS
        self.limb = []
        self.is_stud = False

        # create segments, initialize starting rotations of segments and
        # initialize rotation rates of segments.
        for i in range(self.n_segments):
            self.limb.append(Segment(self.screen))
            self.limb[i].grotation = self.limb[i].rotation = randrange(0, 360)
            self.limb[i].rot_rate = random()

        self.limb[0].is_first = True
        self.limb[-1].is_last = True
        self.reset_location()

    # reset location to bottom of screen
    def reset_location(self):
        self.limb[0].bx = RESET_X_OFFSET + self.cid * RESET_X_MUL
        self.limb[0].by = RESET_Y

        for i in range(self.n_segments):
            self.limb[i].rotation = self.limb[i].grotation
            self.limb[i].sforward = True

        self.update()

    def new_ex(self, i):
        return int(self.limb[i].length * math.sin(self.limb[i].rotation * (math.pi / 180.0)))

    def new_ey(self, i):
        return int(self.limb[i].length * math.cos(self.limb[i].rotation * (math.pi / 180.0)))

    # update location of segments
    def update(self):

        # for each segment
        for i in range(self.n_segments):

            # update segment
            self.limb[i].update()

            # if swinging forward
            if self.limb[i].sforward:

                # if not first
                if i > 0:

                    # set beginning of segment to previous segments endpoints
                    self.limb[i].bx = self.limb[i-1].ex
                    self.limb[i].by = self.limb[i-1].ey

                # calculate new endpoints
                self.limb[i].ex = self.limb[i].bx + self.new_ex(i)
                self.limb[i].ey = self.limb[i].by + self.new_ey(i)

            # if swinging back
            else:

                # if not last
                if i < self.n_segments-1:

                    # set endpoints to next segments beginning points
                    self.limb[i].ex = self.limb[i+1].bx
                    self.limb[i].ey = self.limb[i+1].by

                # calculate new beginning points
                self.limb[i].bx = self.limb[i].ex - self.new_ex(i)
                self.limb[i].by = self.limb[i].ey - self.new_ey(i)

    # draw all the segments
    def draw(self):
        if self.is_stud:
            self.limb[0].is_stud = True

        for i in range(self.n_segments):
            self.limb[i].draw()

    # return a mutation
    @staticmethod
    def mutate():
        if randrange(CHANCE) == 1:
            return random() - 0.5
        else:
            return 0.0

    # return location of head
    def get_loc(self):
        return self.limb[0].bx, self.limb[0].by

    # breed: # for each segment blend and mutate with winner
    def breedwith(self, stud):
        for i in range(self.n_segments):
            self.limb[i].rotation = (self.limb[i].rotation +
                                     stud.limb[i].grotation) / 2 + self.mutate()
            self.limb[i].grotation = self.limb[i].rotation

            self.limb[i].rot_rate = (stud.limb[i].rot_rate +
                                     self.limb[i].rot_rate) / 2 + self.mutate()
