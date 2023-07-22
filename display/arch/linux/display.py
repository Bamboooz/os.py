# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess


def resolution() -> tuple:
    result = subprocess.run(["xrandr"], capture_output=True, text=True)

    resolution_format = result.stdout.splitlines()[0].replace(" ", "").split(",")

    resolution = None

    for item in resolution_format:
        if item.startswith("current"):
            resolution = item.replace("current", "")

    if not resolution:
        return None

    x, y = tuple(resolution.split("x"))
    return int(x), int(y)


def refreq() -> float:
    result = subprocess.run(["xrandr"], capture_output=True, text=True)

    resolution_format = result.stdout.splitlines()[0].replace(" ", "").split(",")

    resolution = None
    refreq = None

    for item in resolution_format:
        if item.startswith("current"):
            resolution = item.replace("current", "")

    if not resolution:
        return None

    for item in result.stdout.splitlines():
        if item.strip().startswith(resolution):
            refreq = item.strip().split()[-1]

    if not refreq: 
        return None

    return float(refreq)
