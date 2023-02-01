from screeninfo import get_monitors
from Xlib import display
from Xlib.ext import randr


def display_device():
    for m in get_monitors():
        data = str(m).replace('Monitor(', '').replace(')', '')
        lst = data.split(', ')
        for i in lst:
            if i.startswith('name'):
                return i.replace("'", "").replace('name=', '')


def screen_resolution():
    for m in get_monitors():
        data = str(m).replace('Monitor(', '').replace(')', '')
        lst = data.split(', ')
        screen_size = ''
        for i in lst:
            if not i == lst[len(lst) - 1]:
                if i.startswith('width') and not i.startswith('width_mm'):
                    screen_size = screen_size + i
                elif i.startswith('height') and not i.startswith('height_mm'):
                    screen_size = screen_size + 'x' + i
            else:
                return screen_size.replace('width=', '').replace('height=', '')


def screen_refresh_frequency():
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
            return str(round(mode.dot_clock / (mode.h_total * mode.v_total))) + 'Hz'
