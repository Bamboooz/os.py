# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from Xlib import display
from Xlib.ext import randr


def resolution() -> tuple:
    d = display.Display()
    root = d.screen().root
    width = root.get_geometry().width
    height = root.get_geometry().height
    return width, height


def refreq() -> int:
    d = display.Display()
    default_screen = d.get_default_screen()
    info = d.screen(default_screen)

    resources = randr.get_screen_resources(info.root)
    active_modes = set()

    for crtc in resources.crtcs:
        crtc_info = randr.get_crtc_info(info.root, crtc, resources.config_timestamp)
        if crtc_info.mode:
            active_modes.add(crtc_info.mode)

    for mode in resources.modes:
        if mode.id in active_modes:
            return round(mode.dot_clock / (mode.h_total * mode.v_total))

    return 0