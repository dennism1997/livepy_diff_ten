from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import ButtonElement
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent


def quantize(num):
    return round(num / 4.0) * 4.0


class LooperComponent(ControlSurfaceComponent):
    """Handles looping controls"""
    __module__ = __name__

    def __init__(self, parent, *a, **k):
        super(LooperComponent, self).__init__(*a, **k)

        self._parent = parent
        self._loop_in_button = None
        self._loop_out_button = None
        self._loop_double_button = None
        self._loop_halve_button = None
        self._clip_length = 0
        self._shift_button = None
        self._current_clip = None
        self._shift_pressed = False

    def get_loop_length(self):
        if self._current_clip is not None:
            clip = self._current_clip
            return clip.loop_end - clip.loop_start
        else:
            return 0

    def set_loop_on_button(self, button):
        assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if self._loop_in_button != button:
            if self._loop_in_button is not None:
                self._loop_in_button.remove_value_listener(self.start_loop)
            self._loop_in_button = button
            if self._loop_in_button is not None:
                self._loop_in_button.add_value_listener(self.start_loop)

    def start_loop(self, value):
        # toggles loop, sets start point to the current playing position
        if value > 0:
            self.get_current_clip()
            if self._current_clip is not None:
                current_clip = self._current_clip
                if current_clip.looping == 1:
                    current_clip.looping = 0
                else:
                    if self._clip_length == 0:
                        self._clip_length = current_clip.length
                    current_position = current_clip.playing_position
                    current_clip.looping = 1
                    # set end to the end of the song for now
                    current_clip.loop_end = quantize(self._clip_length)
                    # set start to the current position
                    current_clip.loop_start = quantize(current_position)

    def set_loop_off_button(self, button):
        assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if self._loop_out_button != button:
            if self._loop_out_button is not None:
                self._loop_out_button.remove_value_listener(self.stop_loop)
            self._loop_out_button = button
            if self._loop_out_button is not None:
                self._loop_out_button.add_value_listener(self.stop_loop)

    def stop_loop(self, value):
        # sets end point to the current playing position
        if value > 0:
            self.get_current_clip()
            if self._current_clip is not None:
                current_clip = self._current_clip
                current_position = current_clip.playing_position
                current_clip.loop_end = quantize(current_position)

    def set_loop_double_button(self, button):
        assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if self._loop_double_button != button:
            if self._loop_double_button is not None:
                self._loop_double_button.remove_value_listener(self.increase_loop)
            self._loop_double_button = button
            if self._loop_double_button is not None:
                self._loop_double_button.add_value_listener(self.increase_loop)

    # Doubles loop with shift
    # Moves loop one bar right without shift
    def increase_loop(self, value):
        if value > 0:
            self.get_current_clip()
            if self._current_clip is not None:
                current_clip = self._current_clip
                loop_length = self.get_loop_length()
                if self._shift_pressed:
                    current_clip.loop_end = current_clip.loop_start + loop_length * 2.0
                else:
                    current_clip.loop_end = current_clip.loop_end + 4.0
                    current_clip.loop_start = current_clip.loop_start + 4.0

    def set_loop_halve_button(self, button):
        assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if self._loop_halve_button != button:
            if self._loop_halve_button is not None:
                self._loop_halve_button.remove_value_listener(self.decrease_loop)
            self._loop_halve_button = button
            if self._loop_halve_button is not None:
                self._loop_halve_button.add_value_listener(self.decrease_loop)

    # halves loop with shift
    # left loop one bar right without shift
    def decrease_loop(self, value):
        if value > 0:
            self.get_current_clip()
            if self._current_clip is not None:
                current_clip = self._current_clip
                loop_length = self.get_loop_length()
                if self._shift_pressed:
                    current_clip.loop_end = current_clip.loop_start + loop_length / 2.0
                else:
                    if current_clip.loop_start >= 4.0:
                        current_clip.loop_end = current_clip.loop_end - 4.0
                        current_clip.loop_start = current_clip.loop_start - 4.0
                    else:
                        current_clip.loop_end = 0.0 + loop_length
                        current_clip.loop_start = 0.0

    def get_current_clip(self):
        if self._parent.song().view.highlighted_clip_slot is not None:
            clip_slot = self._parent.song().view.highlighted_clip_slot
            if clip_slot.has_clip:
                self._current_clip = clip_slot.clip
            else:
                self._current_clip = None
        else:
            self._current_clip = None

    def set_shift_button(self, button):  # added
        assert ((button is None) or (isinstance(button, ButtonElement) and button.is_momentary()))
        if self._shift_button != button:
            if self._shift_button is not None:
                self._shift_button.remove_value_listener(self._shift_value)
            self._shift_button = button
            if self._shift_button is not None:
                self._shift_button.add_value_listener(self._shift_value)

    def _shift_value(self, value):  # added
        assert (self._shift_button is not None)
        assert (value in range(128))
        self._shift_pressed = (value != 0)
