from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import Color

class AnimatedColor(Color):
    _channel = None

    def __init__(self, color1 = None, color2 = None, *a, **k):
        super(AnimatedColor, self).__init__(*a, **k)
        self._color1 = color1
        self._color2 = color2

    def draw(self, interface):
        interface.send_value(self._color1.midi_value)
        interface.send_value(self._color2.midi_value, channel=self._channel)


class Pulse(AnimatedColor):
    _channel = 2


class Blink(AnimatedColor):
    _channel = 1


class Rgb:
    BLACK = Color(0)
    WHITE = Color(3)
    GREEN = Color(21)
    GREEN_BLINK = Blink(color1=BLACK, color2=GREEN)
    GREEN_PULSE = Pulse(color1=BLACK, color2=GREEN)
    AMBER = Color(96)
    RED = Color(5)
    RED_BLINK = Blink(color1=BLACK, color2=RED)
    RED_PULSE = Pulse(color1=BLACK, color2=RED)
    YELLOW = Color(13)
    LIGHT_BLUE = Color(37)
    DARK_BLUE = Color(49)
    DARK_ORANGE = Color(84)


CLIP_COLOR_TABLE = {15549221: 60,
 12411136: 61,
 11569920: 62,
 8754719: 63,
 5480241: 64,
 695438: 65,
 31421: 66,
 197631: 67,
 3101346: 68,
 6441901: 69,
 8092539: 70,
 3947580: 71,
 16712965: 72,
 12565097: 73,
 10927616: 74,
 8046132: 75,
 4047616: 76,
 49071: 77,
 1090798: 78,
 5538020: 79,
 8940772: 80,
 10701741: 81,
 12008809: 82,
 9852725: 83,
 16149507: 84,
 12581632: 85,
 8912743: 86,
 1769263: 87,
 2490280: 88,
 6094824: 89,
 1698303: 90,
 9160191: 91,
 9611263: 92,
 12094975: 93,
 14183652: 94,
 16726484: 95,
 16753961: 96,
 16773172: 97,
 14939139: 98,
 14402304: 99,
 12492131: 100,
 9024637: 101,
 8962746: 102,
 10204100: 103,
 8758722: 104,
 13011836: 105,
 15810688: 106,
 16749734: 107,
 16753524: 108,
 16772767: 109,
 13821080: 110,
 12243060: 111,
 11119017: 112,
 13958625: 113,
 13496824: 114,
 12173795: 115,
 13482980: 116,
 13684944: 117,
 14673637: 118,
 16777215: 119}
RGB_COLOR_TABLE = ((0, 0),
 (1, 1973790),
 (2, 8355711),
 (3, 16777215),
 (4, 16731212),
 (5, 16711680),
 (6, 5832704),
 (7, 1638400),
 (8, 16760172),
 (9, 16733184),
 (10, 5840128),
 (11, 2562816),
 (12, 16777036),
 (13, 16776960),
 (14, 5855488),
 (15, 1644800),
 (16, 8978252),
 (17, 5570304),
 (18, 1923328),
 (19, 1321728),
 (20, 5046092),
 (21, 65280),
 (22, 22784),
 (23, 6400),
 (24, 5046110),
 (25, 65305),
 (26, 22797),
 (27, 6402),
 (28, 5046152),
 (29, 65365),
 (30, 22813),
 (31, 7954),
 (32, 5046199),
 (33, 65433),
 (34, 22837),
 (35, 6418),
 (36, 5030911),
 (37, 43519),
 (38, 16722),
 (39, 4121),
 (40, 5015807),
 (41, 22015),
 (42, 7513),
 (43, 2073),
 (44, 5000447),
 (45, 255),
 (46, 89),
 (47, 25),
 (48, 8867071),
 (49, 5505279),
 (50, 1638500),
 (51, 983088),
 (52, 16731391),
 (53, 16711935),
 (54, 5832793),
 (55, 1638425),
 (56, 16731271),
 (57, 16711764),
 (58, 5832733),
 (59, 2228243),
 (60, 16717056),
 (61, 10040576),
 (62, 7950592),
 (63, 4416512),
 (64, 211200),
 (65, 22325),
 (66, 21631),
 (67, 255),
 (68, 17743),
 (69, 2425036),
 (70, 8355711),
 (71, 2105376),
 (72, 16711680),
 (73, 12451629),
 (74, 11529478),
 (75, 6618889),
 (76, 1084160),
 (77, 65415),
 (78, 43519),
 (79, 11007),
 (80, 4129023),
 (81, 7995647),
 (82, 11672189),
 (83, 4202752),
 (84, 16730624),
 (85, 8970502),
 (86, 7536405),
 (87, 65280),
 (88, 3931942),
 (89, 5898097),
 (90, 3735500),
 (91, 5999359),
 (92, 3232198),
 (93, 8880105),
 (94, 13835775),
 (95, 16711773),
 (96, 16744192),
 (97, 12169216),
 (98, 9502464),
 (99, 8609031),
 (100, 3746560),
 (101, 1330192),
 (102, 872504),
 (103, 1381674),
 (104, 1450074),
 (105, 6896668),
 (106, 11010058),
 (107, 14569789),
 (108, 14182940),
 (109, 16769318),
 (110, 10412335),
 (111, 6796559),
 (112, 1973808),
 (113, 14483307),
 (114, 8454077),
 (115, 10131967),
 (116, 9332479),
 (117, 4210752),
 (118, 7697781),
 (119, 14745599),
 (120, 10485760),
 (121, 3473408),
 (122, 1757184),
 (123, 475648),
 (124, 12169216),
 (125, 4141312),
 (126, 11755264),
 (127, 4920578))
