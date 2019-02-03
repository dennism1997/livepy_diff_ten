from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {u'STOP': GENERIC_STOP,
 u'PLAY': GENERIC_PLAY,
 u'REC': GENERIC_REC,
 u'LOOP': GENERIC_LOOP,
 u'RWD': GENERIC_RWD,
 u'FFWD': GENERIC_FFWD,
 u'NORELEASE': 0}
DEVICE_CONTROLS = ((GENERIC_ENC1, 0),
 (GENERIC_ENC2, 0),
 (GENERIC_ENC3, 0),
 (GENERIC_ENC4, 0),
 (GENERIC_ENC5, 0),
 (GENERIC_ENC6, 0),
 (GENERIC_ENC7, 0),
 (GENERIC_ENC8, 0))
VOLUME_CONTROLS = ((GENERIC_SLI1, 0),
 (GENERIC_SLI2, 0),
 (GENERIC_SLI3, 0),
 (GENERIC_SLI4, 0),
 (GENERIC_SLI5, 0),
 (GENERIC_SLI6, 0),
 (GENERIC_SLI7, 0),
 (GENERIC_SLI8, 0))
TRACKARM_CONTROLS = (GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {u'TOGGLELOCK': -1,
 u'BANKDIAL': -1,
 u'NEXTBANK': -1,
 u'PREVBANK': -1,
 u'BANK1': -1,
 u'BANK2': -1,
 u'BANK3': -1,
 u'BANK4': -1,
 u'BANK5': -1,
 u'BANK6': -1,
 u'BANK7': -1,
 u'BANK8': -1}
PAD_TRANSLATION = ((0, 0, 48, 0),
 (1, 0, 49, 0),
 (2, 0, 50, 0),
 (3, 0, 51, 0),
 (0, 1, 44, 0),
 (1, 1, 45, 0),
 (2, 1, 46, 0),
 (3, 1, 47, 0),
 (0, 2, 40, 0),
 (1, 2, 41, 0),
 (2, 2, 42, 0),
 (3, 2, 43, 0),
 (0, 3, 36, 0),
 (1, 3, 37, 0),
 (2, 3, 38, 0),
 (3, 3, 39, 0))
CONTROLLER_DESCRIPTION = {u'INPUTPORT': u'Akai MPD18',
 u'OUTPUTPORT': u'Akai MPD18',
 u'CHANNEL': 0,
 u'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {u'NUMSENDS': 2,
 u'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
 u'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
 u'MASTERVOLUME': 1}