from __future__ import absolute_import, print_function, unicode_literals
from __future__ import division
from past.utils import old_div
TIMER_DELAY = 0.1
MOMENTARY_DELAY = 0.3
MOMENTARY_DELAY_TICKS = int(old_div(MOMENTARY_DELAY, TIMER_DELAY))
