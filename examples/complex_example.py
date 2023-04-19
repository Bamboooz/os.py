# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from tkinter import *
from tkinter.scrolledtext import ScrolledText

from ospy import *


def print_text():
    text_area.configure(state="normal")

    for key, value in sys.get_os_info().items():
        text_area.insert(END, f"os {key}: {value}\n")

    for key, value in cpu.get_processor_info().items():
        text_area.insert(END, f"cpu {key}: {value}\n")

    for key, value in gpu.get_graphics_card_info().items():
        text_area.insert(END, f"gpu {key}: {value}\n")

    for key, value in memory.get_ram_info().items():
        text_area.insert(END, f"ram {key}: {value}\n")

    text_area.insert(END, f'available drives {storage.get_drive_list()}\n')

    for key, value in storage.get_drive_info().items():
        text_area.insert(END, f"storage {key}: {value}\n")

    for key, value in motherboard.get_motherboard_info().items():
        text_area.insert(END, f"motherboard {key}: {value}\n")

    text_area.insert(END, f'number of connected external devices: {device.get_number_of_external_drives()}\n')
    text_area.insert(END, f'external drives: {device.get_external_drives()}\n')
    text_area.insert(END, f'firmware type: {machine.get_firmware_type()}\n')

    text_area.configure(state="disabled")

if __name__ == '__main__':
    # complex_example.py - tkinter windows presenting all information that os.py could gather
    window = Tk()
    window.title("complex_example.py")
    window.configure(bg="#333333")

    # Create the text area
    text_area = ScrolledText(window, height=30, state="disabled", bg="#1F1F1F", fg="#FFFFFF")
    text_area.pack(fill=BOTH, expand=True)

    print_text()
    window.mainloop()
