#!/usr/bin/env python2

"""
Template for a RadioPyo song (version 1.0).
"""
import sys

from math import pow
from pyo import *

################### USER-DEFINED VARIABLES ###################
### READY is used to manage the server behaviour depending ###
### of the context. Set this variable to True when the     ###
### music is ready for the radio. TITLE and ARTIST are the ###
### infos shown by the radio player. DURATION set the      ###
### duration of the audio file generated for the streaming.###
##############################################################
READY = True           # Set to True when ready for the radio
TITLE = "Echo Pastorale"    # The title of the music
ARTIST = "Aaron Krister Johnson"  # Your artist name
DURATION = 234         # The duration of the music in seconds
##################### These are optional #####################
GENRE = "Electronic Neo-Baroque" # Kind of your music, if there is any
DATE = 2017                      # Year of creation

####################### SERVER CREATION ######################
if READY:
    s = Server(duplex=0, audio="offline").boot()
    s.recordOptions(dur=DURATION, filename=sys.argv[1], fileformat=7)
else:
    s = Server(duplex=0).boot()

##################### PROCESSING SECTION #####################
# global volume (should be used to control the overall sound)
fade = Fader(fadein=0.01, fadeout=2, dur=DURATION, mul=0.49).play()

##################################################################### 
# CODE.                                                             # 
# This is a neo-baroque piece. It consists of two treble lines      #
# in strict canon, with an obbligato bass line. The score is        # 
# constructed by making use of the packing and unpacking of tuples, #
# which allowed me to keep track of individual note events, while   #
# unpacking them later for use by 'Seq' objects.                    #
# ###################################################################
TICK = 1.08 / 24.0
SPEED = 1.0
EDO = 31.0

PITCH_MAP = [('c,,', -62), ('d,,', -57), ('e,,', -52), ('f,,', -49),
             ('g,,', -44), ('a,,', -39), ('_b,,', -36), ('=b,,', -34),
             ('c,', -31), ('d,', -26), ('e,', -21), ('f,', -18), ('g,', -13),
             ('a,', -8), ('_b,', -5), ('c', 0), ('e', 10), ('f', 13),
             ('g', 18), ('a', 23), ('_b', 26), ('=b', 28), ("c'", 31),
             ("d'", 36), ("e'", 41), ("f'", 44), ("g'", 49), ("a'", 54)]

def edo2hz(x, edo=EDO):
    return pow(2, (x + 0.0)/edo) * 256

PITCH_DICT = {x[0]:edo2hz(x[1]) for x in PITCH_MAP}

## performance data:                            

# vol 93
LEAD_A1_1 = [
        (16, "f", 0.93, 1),     (7, "g", 0.93), (1, "g", 0), 
        (16, "a", 0.93),        (7, "_b", 0.93), (1, "_b", 0),
        (12, "c'", 0.93), (4, "d'", 0.93), (4, "_b", 0.93), (4, "a", 0.93),
        (12, "g", 0.93), (4, "g", 0),  (8, "g", 0.93),
        (16, "_b", 0.93),       (6, "c'", 0.93), (2, "c'", 0),
        (12, "d'", 0.93), (4, "c'", 0.93), (4, "_b", 0.93), (4, "g", 0.93),
        (12,  "a", 0.93),    (4, "a", 0),  (8, "g", 0.93),
        (8, "f", 0.93),  (8, "f", 0),      (8, "_b", 0.93),
        (12, "a", 0.93), (4, "c'", 0.93),  (4, "d'", 0.93), (4, "e'", 0.93),
        (16, "f'", 0.93),              (7, "e'", 0.93), (1, "e'", 0),
        (16, "d'", 0.93),              (7, "c'", 0.93), (1, "c'", 0),
        (12, "d'", 0.93), (4, "e'", 0.93), (7, "f'", 0.93), (1, "f'", 0),
        (16, "_b", 0.93),               (7, "a", 0.93), (1, "a", 0),
        (12, "_b", 0.93), (4, "c'", 0.93),  (8, "d'", 0.93),
        ( 8,  "g", 0.93),     (8, "a", 0.93),  (8, "_b", 0.93),
        (12, "c'", 0.93), (4, "_b", 0.93), (4, "a", 0.93), (4, "g", 0.93)]

#vol 92               
LEAD_A2_1 = [
        (16, "f", 0.92),                (7, "g", 0.92), (1, "g", 0),
        (16, "a", 0.92),                (7, "_b", 0.92), (1, "_b", 0),
        (12, "c'", 0.92), (4, "d'", 0.92), (4, "_b", 0.92), (4, "a", 0.92),
        (12, "g", 0.92), (4, "g", 0),  (8, "g", 0.92),
        (16, "_b", 0.92),               (7, "c'", 0.92), (1, "c'", 0),
        (12, "d'", 0.92), (4, "c'", 0.92), (4, "_b", 0.92), (4, "g", 0.92),
        (12,  "a", 0.92),   (4, "a", 0),   (8, "g", 0.92),
        (12, "f", 0.92),    (4, "f", 0.0), (8, "_b", 0.92),
        (10, "a", 0.92), (2, "a", 0), (4, "c'", 0.92),
                                      (4, "d'", 0.92), (4, "e'", 0.92),
        (16, "f'", 0.92),              (7, "e'", 0.92), (1, "e'", 0),
        (16, "d'", 0.92),              (7, "c'", 0.92), (1, "c'", 0),
        (12, "d'", 0.92), (4, "e'", 0.92), (8, "f'", 0.92),
        (16, "_b", 0.92),               (6, "a", 0.92), (2, "a", 0),
        (12, "_b", 0.92), (4, "c'", 0.92),  (8, "d'", 0.92),
        (8,  "g", 0.92), (8, "a", 0.92),  (8, "=b", 0.92),
        (12, "c'", 0.92), (3, "d'", 0.925), (1, "d'", 0), (4, "d'", 0.93),
                                        (2, "e'", 0.935), (2, "e'", 0)]

#vol 94
LEAD_B_1 = [
        (4, "e'", 0.94), (4, "d'", 0.94), (4, "c'", 0.94), (4, "=b", 0.94), 
                                          (4, "a", 0.94),
                                          (2, "=b", 0.94), (2, "=b", 0),
        (10, "g", 0.94), (2, "g", 0), (2, "g", 0.94), (2, "g", 0), 
                                       (8, "g", 0.94),
        (4,  "c'", 0.94), (4, "d'", 0.94), (4, "e'", 0.94), (4, "c'", 0.94), 
                                          (4, "=b", 0.94), (4, "a", 0.94),
        (12, "g", 0.94),   (4, "a", 0.94), (7, "g", 0.94), (1, "g", 0),
        (12, "e'", 0.94),  (4, "f'", 0.94), (7, "e'", 0.94), (1, "e'", 0),
        (16, "c'", 0.94),           (6, "g", 0.94), (2, "g", 0),
        (12, "g'", 0.94),  (4, "a'", 0.94), (7, "f'", 0.94), (1, "f'", 0),              
        (12, "e'", 0.94),  (4, "f'", 0.94), (8, "d'", 0.94),
        (12, "c'", 0.94),  (4, "d'", 0.94), (4, "e'", 0.94), (4, "f'", 0.94),
        (16, "g'", 0.94),                   (6, "f'", 0.94), (2, "f'", 0),
        (16, "e'", 0.94),                   (6, "d'", 0.94), (2, "d'", 0),
        (4, "c'", 0.94), (4, "=b", 0.94), (4, "c'", 0.94), (4, "d'", 0.94), 
                                          (4, "e'", 0.94), (4, "f'", 0.94),
        (8, "g'", 0.94), (4, "g'", 0), (2, "g'", 0.94), (2, "g'", 0), 
                                    (2, "g'", 0.94), (2, "g'", 0), 
                                    (2, "g'", 0.94), (2, "g'", 0),
        (6, "e'", 0.94), (2, "e'", 0),  (16, "e'", 0.94),
        (12, "c'", 0.94), (4, "a", 0.94), (4, "g", 0.94), (4, "f", 0.94),
        (12, "e", 0.94), (4, "f", 0.94), (4, "e", 0.94), (4, "e", 0),
        (12, "g", 0.94), (4, "a", 0.94), (4, "g", 0.94), (4, "g", 0.94),
        (10, "e'", 0.94), (2, "e'", 0), (4, "f'", 0.94), (4, "e'", 0.94), (4, "d'", 0.94),
        (16, "c'", 0.94),               (8, "=b", 0.94),
        (12, "c'", 0.94), (4, "d'", 0.94), (8, "e'", 0.94),
        (16, "a", 0.94),                (7, "g", 0.94), (1, "g", 0),
        (12, "a", 0.94), (4, "=b", 0.94),  (8, "c'", 0.94),
        (24, "f", 0.94), 
        (16, "d'", 0.94),               (7, "c'", 0.94), (1, "c'", 0),
        (16, "=b", 0.94),               (6, "a", 0.94), (2, "a", 0),
        (12, "=b", 0.94), (4, "c'", 0.94), (8, "d'", 0.94), 
        (12, "g", 0.94),  (4, "a", 0.94),  (6, "g", 0.94), (2, "g", 0),
        (12, "e'", 0.94), (4, "e'", 0), (8, "e'", 0.94),
        (12, "c'", 0.94), (4, "d'", 0.94), (7, "=b", 0.94), (1, "=b", 0),
        (12, "a", 0.94),  (4, "c'", 0.94), (4, "d'", 0.94), (4, "e'", 0.94),
        (12, "f'", 0.94), (4, "g'", 0.94), (6, "e'", 0.94), (2, "e'", 0),
        (12, "d'", 0.94), (4, "e'", 0.94), (7, "c'", 0.94), (1, "c'", 0),
        (12, "=b", 0.94), (1, "=b", 0.0), (4, "d'", 0.94), (4, "e'", 0.94),
                                          (4, "f'", 0.94),
        (12, "g'", 0.94), (4, "a'", 0.94), (7, "f'", 0.94), (1, "f'", 0),
        (4, "e'", 0.94), (4, "e'", 0.94),
          (4, "e'", 0.94), (4, "f'", 0.94),
          (4, "d'", 0.94), (3, "d'", 0.94), (1, "d'", 0.0),
        (4, "c'", 0.94), (4, "c'", 0.94), 
          (2, "c'", 0.94), (2, "c'", 0), (4, "e'", 0.94), 
          (4, "f'", 0.94, 1), (4, "g'", 0.94),
        # PEAK!
        (4, "a'", 0.94), (4, "a'", 0.94), 
          (4, "a'", 0.94), (4, "g'", 0.94, 1), 
          (6, "a'", 0.94), (2, "a'", 0),
        (4, "f'", 0.94), (4, "g'", 0.94), (4, "f'", 0.94), (4, "e'", 0.94), 
                                          (4, "f'", 0.94), (4, "e'", 0.94),
        (4, "d'", 0.94), (4, "e'", 0.94), (4, "d'", 0.94), (4, "c'", 0.94), 
                                          (4, "d'", 0.94), (4, "c'", 0.94),
        (4, "=b", 0.94), (4, "c'", 0.94), (4, "d'", 0.94), (4, "d'", 0), 
                                           (4, "=b", 0.94), (4, "=b", 0),
        (12, "g'", 0.94),                 (4, "f'", 0.94), (6, "g'", 0.94),
                                                            (2, "g'", 0),
        (4, "e'", 0.94), (4, "f'", 0.94), (4, "e'", 0.94), (4, "d'", 0.94),
                                          (4, "e'", 0.94), (4, "d'", 0.94),
        (4, "c'", 0.94), (4, "d'", 0.94), (4, "c'", 0.94), (4, "=b", 0.94), 
                                          (4, "c'", 0.94), (4, "=b", 0.94),
        (4, "a", 0.94),  (4, "=b", 0.94), (4, "c'", 0.94), (4, "c'", 0), 
                                          (4, "a", 0.94),  (4, "a", 0),
        (12, "f'", 0.94),  (4, "e'", 0.94), (6, "f'", 0.94), (2, "f'", 0),
        (4, "d'", 0.94), (4, "e'", 0.94), (4, "d'", 0.94), (4, "c'", 0.94),
                                          (4, "d'", 0.94), (4, "c'", 0.94),
        (4, "=b", 0.94), (4, "c'", 0.94), (4, "=b", 0.94), (4, "a", 0.94), 
                                          (4, "=b", 0.94), (4, "c'", 0.94),
        (12, "d'", 0.94),      (4, "d'", 0), (2, "d'", 0.94), (2, "d'", 0),
                                             (4, "d'", 0.94),
        (12, "f", 0.94),        (4, "g", 0.94),  (4, "a", 0.94), 
                                                 (4, "=b", 0.94),
        (12, "c'", 0.94), (4, "=b", 0.94), (4, "c'", 0.94), (4, "c'", 0), 
        (4,  "e", 0.94),  (4, "e", 0.94),
          (4, "g", 0.94), (4, "g", 0.94),  
          (4, "g", 0),    (4, "g", 0),
        (4, "c'", 0.94), (4, "c'", 0.94),
           (4, "c'", 0.94), (4, "_b", 0.935), 
           (4, "a", 0.93), (4, "g", 0.92)]
#vol 90
LEAD_A1_2 = [        
        (4, "f", 0.90), (4, "f", 0.90),
          (4, "f", 0.90), (4, "f", 0.90),
          (7, "g", 0.90), (1, "g", 0), 
        (16, "a", 0.90),  (7, "_b", 0.90), (1, "_b", 0),
        (12, "c'", 0.90), (4, "d'", 0.90), (4, "_b", 0.90), (4, "a", 0.90),
        (12, "g", 0.90), (4, "g", 0),  (8, "g", 0.90),
        (16, "_b", 0.90),       (6, "c'", 0.90), (2, "c'", 0),
        (12, "d'", 0.90), (4, "c'", 0.90), (4, "_b", 0.90), (4, "g", 0.90),
        (12,  "a", 0.90),     (4, "a", 0), (8, "g", 0.90),
        (8, "f", 0.90),  (8, "f", 0.0),    (8, "_b", 0.90),
        (12, "a", 0.90), (4, "c'", 0.90), (4, "d'", 0.90), (4, "e'", 0.90),
        (16, "f'", 0.90),              (7, "e'", 0.90), (1, "e'", 0),
        (16, "d'", 0.90),              (7, "c'", 0.90), (1, "c'", 0),
        (12, "d'", 0.90), (4, "e'", 0.90), (7, "f'", 0.90), (1, "f'", 0),
        (16, "_b", 0.90),               (7, "a", 0.90), (1, "a", 0),
        (12, "_b", 0.90), (4, "c'", 0.90),  (8, "d'", 0.90),
        ( 8,  "g", 0.90),     (8, "a", 0.90),  (8, "_b", 0.90),
        (12, "c'", 0.90), (4, "_b", 0.90), (4, "a", 0.89), (4, "g", 0.89)]

#vol 88
LEAD_A2_2 = [
        (16, "f", 0.88),                (7, "g", 0.88), (1, "g", 0),
        (16, "a", 0.88),                (7, "_b", 0.88), (1, "_b", 0),
        (12, "c'", 0.88), (4, "d'", 0.88), (4, "_b", 0.88), (4, "a", 0.88),
        (12, "g", 0.88), (4, "g", 0),  (8, "g", 0.88),
        (16, "_b", 0.88),               (7, "c'", 0.88), (1, "c'", 0),
        (12, "d'", 0.88), (4, "c'", 0.88), (4, "_b", 0.88), (4, "g", 0.88),
        (10,  "a", 0.88),   (6, "a", 0),  (8, "g", 0.88),
        (12, "f", 0.88),    (4, "f", 0),  (8, "_b", 0.88),
        (10, "a", 0.88), (2, "a", 0), (4, "c'", 0.88), 
                                      (4, "d'", 0.88), (4, "e'", 0.88),
        (16, "f'", 0.88),              (7, "e'", 0.88), (1, "e'", 0),
        (16, "d'", 0.88),              (7, "c'", 0.88), (1, "c'", 0),
        (12, "d'", 0.88), (4, "e'", 0.88), (8, "f'", 0.88),
        (16, "_b", 0.88),               (6, "a", 0.88), (2, "a", 0),
        (12, "_b", 0.88), (4, "c'", 0.88),  (8, "d'", 0.88),
        (8,  "g", 0.88), (8, "a", 0.88),  (8, "=b", 0.88),
        (12, "c'", 0.88), (3, "d'", 0.89), (1, "d'", 0), (4, "d'", 0.903),
                                        (2, "e'", 0.907), (2, "e'", 0)]

#vol 0.93-0.97
LEAD_B_2 = [
        (4, "e'", 0.91), (4, "d'", 0.91), (4, "c'", 0.912), (4, "=b", 0.914), 
                                          (4, "a", 0.916),
                                          (2, "=b", 0.918), (2, "=b", 0),
        (10, "g", 0.92), (2, "g", 0), (2, "g", 0.923), (2, "g", 0), 
                                       (8, "g", 0.927),
        (4,  "c'", 0.93), (4, "d'", 0.932), (4, "e'", 0.934), (4, "c'", 0.936), 
                                          (4, "=b", 0.938), (4, "a", 0.939),
        (12, "g", 0.94),   (4, "a", 0.943), (7, "g", 0.947), (1, "g", 0),
        (12, "e'", 0.95),  (4, "f'", 0.953), (7, "e'", 0.957), (1, "e'", 0),
        (16, "c'", 0.96),             (6, "g", 0.96), (2, "g", 0),
        (12, "g'", 0.97),  (4, "a'", 0.97), (7, "f'", 0.97), (1, "f'", 0),              
        (12, "e'", 0.97),  (4, "f'", 0.97), (8, "d'", 0.97),
        (12, "c'", 0.97),  (4, "d'", 0.97), (4, "e'", 0.97), (4, "f'", 0.97),
        (16, "g'", 0.97),                   (6, "f'", 0.97), (2, "f'", 0),
        (16, "e'", 0.97),                   (6, "d'", 0.97), (2, "d'", 0),
        (4, "c'", 0.97), (4, "=b", 0.97), (4, "c'", 0.97), (4, "d'", 0.97), 
                                          (4, "e'", 0.97), (4, "f'", 0.97),
        (8, "g'", 0.97), (4, "g'", 0), (2, "g'", 0.97), (2, "g'", 0), 
                                    (2, "g'", 0.97), (2, "g'", 0), 
                                    (2, "g'", 0.97), (2, "g'", 0),
        (6, "e'", 0.97), (2, "e'", 0),  (16, "e'", 0.97),
        (12, "c'", 0.97), (4, "a", 0.97), (4, "g", 0.97), (4, "f", 0.97),
        (12, "e", 0.97), (4, "f", 0.97), (4, "e", 0.97), (4, "e", 0),
        (12, "g", 0.97), (4, "a", 0.97), (4, "g", 0.97), (4, "g", 0.97),
        (10, "e'", 0.97), (2, "e'", 0), (4, "f'", 0.97), (4, "e'", 0.97),
                                        (4, "d'", 0.97),
        (16, "c'", 0.97),               (8, "=b", 0.97),
        (12, "c'", 0.97), (4, "d'", 0.97), (8, "e'", 0.97),
        (16, "a", 0.97),                (7, "g", 0.97), (1, "g", 0),
        (12, "a", 0.97), (4, "=b", 0.97),  (8, "c'", 0.97),
        (24, "f", 0.97), 
        (16, "d'", 0.97),               (7, "c'", 0.97), (1, "c'", 0),
        (16, "=b", 0.97),               (6, "a", 0.97), (2, "a", 0),
        (12, "=b", 0.97), (4, "c'", 0.97), (8, "d'", 0.97), 
        (12, "g", 0.97),  (4, "a", 0.97),  (6, "g", 0.97), (2, "g", 0),
        (12, "e'", 0.97), (4, "e'", 0), (8, "e'", 0.97),
        (12, "c'", 0.97), (4, "d'", 0.97), (7, "=b", 0.97), (1, "=b", 0),
        (12, "a", 0.97),  (4, "c'", 0.97), (4, "d'", 0.97), (4, "e'", 0.97),
        (12, "f'", 0.97), (4, "g'", 0.97), (6, "e'", 0.97), (2, "e'", 0),
        (12, "d'", 0.97), (4, "e'", 0.97), (7, "c'", 0.97), (1, "c'", 0),
        (11, "=b", 0.97), (1, "=b", 0.0), (4, "d'", 0.97), (4, "e'", 0.97),
                                          (4, "f'", 0.97),
        (12, "g'", 0.97), (4, "a'", 0.97), (7, "f'", 0.97), (1, "f'", 0),
        (4, "e'", 0.97), (4, "e'", 0.97),
          (2, "e'", 0.97), (2, "e'", 0.97), (4, "f'", 0.97), 
          (4, "d'", 0.97), (3, "d'", 0.97), (1, "d'", 0.0),
        (4, "c'", 0.97), (4, "c'", 0.97), 
          (2, "c'", 0.85), (2, "c'", 0.0), (4, "e'", 0.97), 
          (4, "f'", 0.97), (4, "g'", 0.97),
        # PEAK!
        (4, "a'", 0.97), (4, "a'", 0.97), 
          (4, "a'", 0.97), (4, "g'", 0.97), 
          (4, "a'", 0.97), (2, "a'", 0.97), (2, "a'", 0),
        (4, "f'", 0.97), (4, "g'", 0.97), (4, "f'", 0.97), (4, "e'", 0.97), 
                                          (4, "f'", 0.97), (4, "e'", 0.97),
        (4, "d'", 0.97), (4, "e'", 0.97), (4, "d'", 0.97), (4, "c'", 0.97), 
                                          (4, "d'", 0.97), (4, "c'", 0.97),
        (4, "=b", 0.97), (4, "c'", 0.97), (4, "d'", 0.97), (4, "d'", 0), 
                                           (4, "=b", 0.97), (4, "=b", 0),
        (12, "g'", 0.97),                 (4, "f'", 0.97), (6, "g'", 0.97),
                                                            (2, "g'", 0),
        (4, "e'", 0.97), (4, "f'", 0.97), (4, "e'", 0.97), (4, "d'", 0.97),
                                          (4, "e'", 0.97), (4, "d'", 0.97),
        (4, "c'", 0.97), (4, "d'", 0.97), (4, "c'", 0.97), (4, "=b", 0.97), 
                                          (4, "c'", 0.97), (4, "=b", 0.97),
        (4, "a", 0.97),  (4, "=b", 0.97), (4, "c'", 0.97), (4, "c'", 0), 
                                          (4, "a", 0.97),  (4, "a", 0),
        (12, "f'", 0.97),  (4, "e'", 0.97), (6, "f'", 0.97), (2, "f'", 0),
        (4, "d'", 0.97), (4, "e'", 0.97), (4, "d'", 0.97), (4, "c'", 0.97),
                                          (4, "d'", 0.97), (4, "c'", 0.97),
        (4, "=b", 0.97), (4, "c'", 0.97), (4, "=b", 0.97), (4, "a", 0.97), 
                                          (4, "=b", 0.97), (4, "c'", 0.97),
        (12, "d'", 0.97),      (4, "d'", 0), (2, "d'", 0.97), (2, "d'", 0),
                                             (4, "d'", 0.97),
        (12, "f", 0.97),        (4, "g", 0.97),  (4, "a", 0.97), 
                                                 (4, "=b", 0.97),
        (12, "c'", 0.97),  (4, "=b", 0.97), (4, "c'", 0.97), (4, "c'", 0), 
        (4, "e", 0.97), (4, "e", 0.97),
          (4, "g", 0.97), (4, "g", 0.97),
          (4, "g", 0, 0.97), (4, "g", 0),
        (4, "c'", 0.96), (4, "c'", 0.96),
          (4, "c'", 0.96), (4, "_b", 0.95), 
          (4, "a", 0.94), (4, "g", 0.93)]

#vol 0.92-0.89
LEAD_A1_3 = [
        (4, "f", 0.92), (4, "f", 0.92),
          (4, "f", 0.92), (4, "f", 0.92),
          (7, "g", 0.91), (1, "g", 0), 
        (16, "a", 0.90),        (7, "_b", 0.89), (1, "_b", 0),
        (12, "c'", 0.89), (4, "d'", 0.89), (4, "_b", 0.89), (4, "a", 0.89),
        (12, "g", 0.89), (4, "g", 0),  (8, "g", 0.89),
        (16, "_b", 0.89),       (6, "c'", 0.89), (2, "c'", 0),
        (12, "d'", 0.89), (4, "c'", 0.89), (4, "_b", 0.89), (4, "g", 0.89),
        (12,  "a", 0.89),     (4, "a", 0), (8, "g", 0.89),
        (12, "f", 0.89),      (4, "f", 0), (8, "_b", 0.89),
        (12, "a", 0.89), (4, "c'", 0.89), (4, "d'", 0.89), (4, "e'", 0.89),
        (16, "f'", 0.89),              (7, "e'", 0.89), (1, "e'", 0),
        (16, "d'", 0.89),              (7, "c'", 0.89), (1, "c'", 0),
        (12, "d'", 0.89), (4, "e'", 0.89), (7, "f'", 0.89), (1, "f'", 0),
        (16, "_b", 0.89),               (7, "a", 0.89), (1, "a", 0),
        (12, "_b", 0.89), (4, "c'", 0.89),  (8, "d'", 0.89),
        ( 8,  "g", 0.89),     (8, "a", 0.89),  (8, "_b", 0.89),
        (12, "c'", 0.89), (4, "_b", 0.88), (4, "a", 0.87), (4, "g", 0.87)]

# 0.87-0.86
LEAD_A2_3= [
        (16, "f", 0.87, 1),     (7, "g", 0.87), (1, "g", 0), 
        (16, "a", 0.86),        (7, "_b", 0.86), (1, "_b", 0),
        (12, "c'", 0.86), (4, "d'", 0.86), (4, "_b", 0.86), (4, "a", 0.86),
        (12, "g", 0.86), (4, "g", 0),  (8, "g", 0.86),
        (16, "_b", 0.86),       (6, "c'", 0.86), (2, "c'", 0),
        (12, "d'", 0.86), (4, "c'", 0.86), (4, "_b", 0.86), (4, "g", 0.86),
        (14,  "a", 0.86),     (2, "a", 0), (8, "g", 0.86),
        (10, "f", 0.86),   (6, "f", 0),    (8, "_b", 0.86),
        (12, "a", 0.86), (4, "c'", 0.86), (4, "d'", 0.86), (4, "e'", 0.86),
        (16, "f'", 0.86),              (7, "e'", 0.86), (1, "e'", 0),
        (16, "d'", 0.86),              (7, "c'", 0.86), (1, "c'", 0),
        (12, "d'", 0.86), (4, "e'", 0.86), (7, "f'", 0.86), (1, "f'", 0),
        (16, "_b", 0.86),               (7, "a", 0.86), (1, "a", 0),
        (12, "_b", 0.86), (4, "c'", 0.86),  (8, "d'", 0.86)]


LEAD_CODA = [
        (8,  "g", 0.86), (8, "a", 0.86),  (8, "_b", 0.86),
        (4, "c'", 0.86), (4, "c'", 0.86), 
          (2, "c'", 0.86), (2, "c'", 0), (4, "a", 0.86),  
          (4, "g", 0.86), (4, "f", 0.86),
        (4, "e", 0.86), (4, "e", 0.86),
          (4, "f", 0.86), (4, "f", 0.86),
          (4, "g", 0.86), (2, "g", 0.86), (2, "g", 0),
        (4, "a", 0.86), (4, "a", 0.86), 
          (4, "a", 0.86), (4, "_b", 0.86),
          (4, "g", 0.86), (2, "g", 0.86), (2, "g", 0),
        (24, "f", 0.86), (12, "f", 0.86)]


###### BASS ######

BASS_A1_1 = [
             (240, "f,", 0.93),
             (24, "_b,,", 0.93),
             (16, "_b,,", 0.93), (8, "a,,", 0.93),
             (48, "g,,", 0.93),
             (12, "d,", 0.93), (12, "f,", 0.93),
             (12, "e,", 0.93), (9, "c,", 0.93), (3, "c,", 0)]

BASS_A2_1 = [
             (24, "c,", 0.92),
             (216, "f,,", 0.92),
             (24, "_b,,", 0.92),
             (16, "_b,,", 0.92), (8, "a,,", 0.92),
             (48, "g,,", 0.92),
             (12, "d,", 0.92), (12, "f,", 0.92),
             (12, "e,", 0.92), (9, "c,", 0.92), (3, "c,", 0)]
             
BASS_B_1 = [
             (144, "c,", 0.94),
             (11*24, "c,,", 0.94),             
             (16, "c,", 0.94), (8, "=b,,", 0.94),
             (24, "a,,", 0.94),
             (16, "a,", 0.94), (8, "g,", 0.94),
             (12, "f,", 0.94), (12, "f,,", 0.94),
             (12, "f,", 0.94), (12, "e,", 0.94),
             (12, "d,", 0.94), (10, "d,,", 0.94), (2, "d,,", 0),
             (12, "d,,", 0.94), (12, "a,,", 0.94),
             (12, "g,,", 0.94), (10, "g,", 0.94), (2, "g,", 0),
             (12, "g,", 0.94), (12, "f,", 0.94),
             (12, "e,", 0.94), (12, "d,", 0.94),
             (12, "c,", 0.94), (4, "d,", 0.94), (6, "c,", 0.94), (2, "c,", 0),
             (12, "c,", 0.94), (10, "f,,", 0.94), (2, "f,,", 0.94),            
             (24, "f,,", 0.94),
             (10, "f,,", 0.94), (2, "f,,", 0), (10, "d,,", 0.94), 
                                                        (2, "d,,", 0),
             (10, "d,,", 0.94), (2, "d,,", 0), (2, "g,,", 0.94), (2, "g,,", 0),
                                            (6, "g,,", 0.94), (2, "g,,", 0),
             (24, "g,,", 0.94),
             (10, "g,,", 0.94), (2, "g,,", 0), (10, "e,,", 0.94), 
                                                         (2, "e,,", 0),
             (10, "e,,", 0.94), (2, "e,,", 0), (2, "a,,", 0.94), (2, "a,,", 0),
                                            (6, "a,,", 0.94), (2, "a,,", 0),
             (22, "a,,", 0.94), (2, "a,,", 0),
             (4, "f,,", 0.94, 0.94), (4, "f,,", 0.94, 0.94),
             (4, "f,,", 0.94, 0.94), (4, "f,,", 0.94, 0.94), 
             (4, "d,,", 0.94, 0.94), (4, "d,,", 0.94, 0.93),
             # PEAK!
             (4, "g,,", 0.94, 1.1),  (4, "g,,", 0.94, 1.1),
               (4, "g,,", 0.94, 1.1), (4, "g,,", 0.94, 1.1),
               (4, "g,,", 0.94), (4, "g,,", 0.94),
             (12, "g,,", 0.94), (4, "g,,", 0.94), (8, "g,,", 0.94), 
             (24*10, "g,,", 0.94),
             (40, "a,,", 0.94), (4, "g,,", 0.94, 0.96), (4, "e,,", 0.94, 0.96),
             (4, "c,,", 0.93, 0.96), (2, "c,,", 0.93, 0.96), (2, "c,,", 0, 1),
               (4, "c,", 0.92, 0.96), (2, "c,", 0.92, 0.95),
                                       (2, "c,", 0, 1),
               (4, "c,,", 0.92, 0.94), (2, "c,,", 0.92, 0.93),
                                       (2, "c,,", 0, 1)]
                          
BASS_A1_2 = [
             (4, "f,,", 0.90, 1.045), (4, "f,,", 0.90, 1.045),
               (4, "f,,", 0.90, 1.045), (4, "f,,", 0.90, 1.045),
               (4, "f,,", 0.90, 1.045), (4, "f,,", 0.90, 1.045),
             (216, "f,,", 0.90),
             (24, "_b,,", 0.90),
             (16, "_b,,", 0.90), (8, "a,,", 0.90),
             (48, "g,,", 0.90),
             (12, "d,", 0.90), (12, "f,", 0.90),
             (12, "e,", 0.90), (9, "c,", 0.90), (3, "c,", 0)]

BASS_A2_2 = [
             (24, "c,", 0.88),
             (216, "f,,", 0.88),
             (24, "_b,,", 0.88),
             (16, "_b,,", 0.88), (8, "a,,", 0.88),
             (48, "g,,", 0.88),
             (12, "d,", 0.88), (12, "f,", 0.88),
             (12, "e,", 0.89), (9, "c,", 0.9), (3, "c,", 0)]
             
BASS_B_2 = [
             (24, "c,", 0.91),
             (24, "c,", 0.92),
             (24, "c,", 0.93),
             (24, "c,", 0.94),
             (24, "c,", 0.95),
             (24, "c,", 0.96),
             (11*24, "c,,", 0.97),             
             (16, "c,", 0.97), (8, "=b,,", 0.97),
             (24, "a,,", 0.97),
             (16, "a,", 0.97), (8, "g,", 0.97),
             (12, "f,", 0.97), (12, "f,,", 0.97),
             (12, "f,", 0.97), (12, "e,", 0.97),
             (12, "d,", 0.97), (10, "d,,", 0.97), (2, "d,,", 0),
             (12, "d,,", 0.97), (12, "a,,", 0.97),
             (12, "g,,", 0.97), (10, "g,", 0.97), (2, "g,", 0),
             (12, "g,", 0.97), (12, "f,", 0.97),
             (12, "e,", 0.97), (12, "d,", 0.97),
             (12, "c,", 0.97), (4, "d,", 0.97), (6, "c,", 0.97), (2, "c,", 0),
             (12, "c,", 0.97), (10, "f,,", 0.97), (2, "f,,", 0.97),            
             (24, "f,,", 0.97),
             (10, "f,,", 0.97), (2, "f,,", 0), (10, "d,,", 0.97), (2, "d,,", 0),
             (10, "d,,", 0.97), (2, "d,,", 0), (2, "g,,", 0.97), (2, "g,,", 0),
                                            (6, "g,,", 0.97), (2, "g,,", 0),
             (24, "g,,", 0.97),
             (10, "g,,", 0.97), (2, "g,,", 0), (10, "e,,", 0.97), (2, "e,,", 0),
             (10, "e,,", 0.97), (2, "e,,", 0), (2, "a,,", 0.97), (2, "a,,", 0),
                                            (6, "a,,", 0.97), (2, "a,,", 0),
             (22, "a,,", 0.97), (2, "a,,", 0),
             (4, "f,,", 0.97, 0.925), (4, "f,,", 0.97, 0.925),
               (4, "f,,", 0.97, 0.925), (4, "f,,", 0.97, 0.925), 
               (4, "d,,", 0.97, 0.925), (2, "d,,", 0.97, 0.925), (2, "d,,", 0.0, 1),
             # PEAK!
             (4, "g,,", 0.97, 1.08), (4, "g,,", 0.97, 1.08),
               (4, "g,,", 0.97, 1.08), (4, "g,,", 0.97, 1.08),
               (4, "g,,", 0.97, 1.08), (4, "g,,", 0.97, 1.08),
             (12, "g,,", 0.97), (4, "g,,", 0.97), (8, "g,,", 0.97), 
             (24*10, "g,,", 0.97),
             (40, "a,,", 0.97), (4, "g,,", 0.96, 0.95), (4, "e,,", 0.95, 0.95),
             (4, "c,,", 0.94, 0.92), (2, "c,,", 0.94, 0.92), (2, "c,,", 0, 1),
               (4, "c,", 0.93, 0.92), (2, "c,", 0.93, 0.92), (2, "c,", 0, 1),
               (4, "c,,", 0.91, 0.91), (2, "c,,", 0.9, 0.9), (2, "c,,", 0, 1)]
             
BASS_A1_3 = [
             (4, "f,,", 0.88, 1.1248), (4, "f,,", 0.88, 1.128),
               (4, "f,,", 0.88, 1.128), (4, "f,,", 0.88, 1.128),
               (4, "f,,", 0.88, 1.128), (4, "f,,", 0.88, 1.128),
             (216, "f,,", 0.88),
             (24, "_b,,", 0.88),
             (16, "_b,,", 0.88), (8, "a,,", 0.88),
             (48, "g,,", 0.88),
             (12, "d,", 0.88), (12, "f,", 0.88),
             (12, "e,", 0.88), (9, "c,", 0.88), (3, "c,", 0)]

BASS_A2_3 = [
             (24, "c,", 0.86, 0.95),
             (216, "f,,", 0.86, 1),
             (24, "_b,,", 0.86, 1),
             (16, "_b,,", 0.86, 1), (8, "a,,", 0.86, 1),
             (48, "g,,", 0.86, 1),
             (12, "d,", 0.86, 1), (12, "f,", 0.86, 1),
             (12, "e,", 0.86, 1), (8, "c,", 0.86, 1), (4, "c,", 0, 1)]
             
BASS_CODA = [
             (4, "a,,", 0.86, 0.962), (4, "a,,", 0.86, 0.962),
               (2, "a,,", 0.86, 0.962), (2, "a,,", 0.86, 0.962), (4, "a,,", 0.86, 0.962),
               (4, "_b,,", 0.86, 0.962), (2, "_b,,", 0.86, 0.962),
                                         (2, "_b,,", 0.86, 1),
             (4, "c,", 0.86, 0.962), (4, "c,", 0.86, 0.962),
               (4, "c,", 0.86, 0.962), (2, "c,", 0.86, 0.952),
                                       (2, "c,", 0, 1),
               (4, "c,,", 0.86, 0.952), (2, "c,,", 0.86, 0.5),
                                       (2, "c,,", 0, 1),
             (4, "f,,", 0.86, 1.62), (4, "f,,", 0.86, 1), 
                                     (4, "f,,", 0.86, 1),
               (4, "f,,", 0.86, 1), (4, "f,,", 0.86, 0.8),
                                      (4, "f,,", 0.86, 1),
             (24, "f,,", 0.86, 0.65),
             (24, "f,,", 0.01)]

## Create form of the piece:
PERF = LEAD_A1_1 + LEAD_A2_1 + \
       LEAD_B_1 + \
       LEAD_A1_2 + LEAD_A2_2 + \
       LEAD_B_2 + \
       LEAD_A1_3 + LEAD_A2_3 + \
       LEAD_CODA

PERF_BASS = BASS_A1_1 + BASS_A2_1 + \
            BASS_B_1 + \
            BASS_A1_2 + BASS_A2_2 + \
            BASS_B_2 + \
            BASS_A1_3 + BASS_A2_3 + \
            BASS_CODA

# convert convenient score to lists for Seq objects:
TIMES = [x[0] for x in PERF]
NOTES = [PITCH_DICT[x[1]] for x in PERF]
VOLS =  [x[2] for x in PERF]

BASS_TIMES = [x[0] for x in PERF_BASS]
BASS_NOTES = [PITCH_DICT[x[1]] for x in PERF_BASS]
BASS_VOLS =  [x[2] for x in PERF_BASS]

######################################
## our instruments are now defined: ##
######################################

# leader
seq_1 = Seq(TICK, TIMES, onlyonce=True).play(delay=TICK * 3)
notes_1 = Iter(seq_1, NOTES)
port_1 = Port(notes_1, risetime=0.005, falltime=0.005)
vol_1 = Iter(seq_1, VOLS, mul=118, add=-119)
vol_1 = DBToA(Sig(vol_1))
volport_1 = Port(vol_1, risetime=0.005, falltime=0.005)
sound_1 = LFO(port_1, type=1, mul=volport_1 * 0.366)
flt_1 = Tone(sound_1, freq=5000 + vol_1 * 8000)
pan_1 = Pan(flt_1, pan=0.15, mul=0.83) #0.9

# echo (canon):
seq_2 = Seq(TICK, TIMES, onlyonce=True).play(delay=TICK * 27)
notes_2 = Iter(seq_2, NOTES)
port_2 = Port(notes_2, risetime=0.005, falltime=0.005)
vol_2 = Iter(seq_2, VOLS, mul=118, add=-119)
vol_2 = DBToA(Sig(vol_2))
volport_2 = Port(vol_2, risetime=0.005, falltime=0.005)
sound_2 = LFO(port_2, type=5, sharp=0.7, mul=volport_2 * 0.32)
flt_2 = Tone(sound_2, freq=5000 + vol_2 * 8000)
pan_2 = Pan(flt_2, pan=0.85) #0.1

## BASS LINE ##
seq_3 = Seq(TICK, BASS_TIMES, onlyonce=True).play(delay=TICK * 3)
notes_3 = Iter(seq_3, BASS_NOTES)
port_3 = Port(notes_3, risetime=0.005, falltime=0.005)
vol_3 = Iter(seq_3, BASS_VOLS, mul=118, add=-119)
vol_3 = DBToA(Sig(vol_3))
volport_3 = Port(vol_3, risetime=0.007, falltime=0.005)
jitter1 = BrownNoise(1.2)
jitter2 = BrownNoise(1.2)
sound_3 = LFO(port_3, type=7, mul=volport_3 * 0.41) #type=7 0.41
sound_4 = LFO((port_3 * 2) + jitter1, type=3, mul=volport_3 * 0.21) #type=7 0.22 0.19
sound_5 = LFO((port_3 * 4) + jitter2, type=7, mul=volport_3 * 0.06) # 0.04 amp
flt_3 = Tone(sound_3, freq=7000 + vol_3 * 8000)
flt_4 = Tone(sound_4, freq=7000 + vol_3 * 8000)
flt_5 = Tone(sound_5, freq=7000 + vol_3 * 8000)
pan_3 = Pan(flt_3, pan=0.5) # 0.5
pan_4 = Pan(flt_4, pan=0.35) # 0.35
pan_5 = Pan(flt_5, pan=0.65) # 0.65
bass_pan = Mix(pan_3+pan_4+pan_5, voices=2, mul=2.4)

###############
### OUTPUT: ###
###############

verb = Freeverb(pan_1+pan_2+bass_pan, size=0.84, damp=0.4, bal=0.4,
                mul=fade)

### MASTERING EQ:
eq_16000 = EQ(verb, freq=16000, boost=17) #18 #16
eq_8000 = EQ(eq_16000, freq=8000, boost=15) #18 #16 #14
eq_4000 = EQ(eq_8000, freq=4000, boost=10) #6 8 12 10
eq_2000 = EQ(eq_4000, freq=2000, boost=3) #3
eq_1000 = EQ(eq_2000, freq=1000, boost=2.3) #3
eq_500 = EQ(eq_1000, freq=500, boost=2.7) #4
eq_250 = EQ(eq_500, freq=250, boost=2.5) #2.5
eq_125 = EQ(eq_250, freq=125, boost=-3) #2.7 5.9 1.7 1.0 -5.0 -2.0
eq_62 = EQ(eq_125, freq=62, boost=2) #3.2 #5 #8 #4 #3.7 #2.7
eq_31 = EQ(eq_62, freq=31, boost=4).out() #0 #10 #5

delayout = Delay(eq_31, delay=0.75, feedback=0.4, maxdelay=1,
                 mul=0.15).out()

### PERFORMANCE CONTROL:
note_count = 0
def ritardando():
    global note_count, SPEED, PERF_BASS, BASS_CODA
    
    if len(PERF_BASS[note_count]) > 3:
        SPEED = PERF_BASS[note_count][3]
        ## reset the speed to new speed factor:
        seq_3.speed *= SPEED
        seq_1.speed = seq_3.speed
        seq_2.speed = seq_3.speed
    else:
        seq_1.speed = 1
        seq_2.speed = 1
        seq_3.speed = 1
    if note_count == len(PERF_BASS) - 1:
        volport_1.setInput(Sig(0))
        volport_2.setInput(Sig(0))
    
    # advance the counter variable:
    note_count += 1
       
cnt = TrigFunc(seq_3, ritardando)

s.setAmp(1.2)
s.start()
