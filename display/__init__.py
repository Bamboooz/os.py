# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


from collections import namedtuple


def display_device() -> namedtuple:
    display_device_format = namedtuple('display_data_format', ['resolution', 'refreq'])
