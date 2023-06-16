# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from ospylib.hardware.arch.windows import memory as _memory
from ospylib.hardware.arch.windows import baseboard as _motherboard


def load_method(methods, function, not_found):
    for source in methods:
        try:
            product = getattr(source(), function)()
            if product is not None and product != "": return product
        except: continue

    return not_found


class baseboard:
    def __init__(self):
        self.sources = [_motherboard.registry, _motherboard.powershell, _motherboard.wmic]

    def product(self) -> str:
        return load_method(self.sources, 'product', '')

    def manufacturer(self) -> str:
        return load_method(self.sources, 'manufacturer', '')

    def version(self) -> str:
        return load_method(self.sources, 'version', '')


class memory:
    def __init__(self):
        self.sources = [_memory.powershell, _memory.wmic]

    def capacity(self) -> dict:
        return load_method(self.sources, 'capacity', {})

    def sticks(self) -> int:
        sticks = self.capacity()
        return len(sticks) if len(sticks) != 0 else -1

    def factor(self) -> dict:
        return load_method(self.sources, 'factor', {})

    def m_type(self) -> dict:
        return load_method(self.sources, 'm_type', {})

    def manufacturer(self) -> dict:
        return load_method(self.sources, 'manufacturer', {})

    def clockspeed(self) -> dict:
        return load_method(self.sources, 'clockspeed', {})

    def serial(self) -> dict:
        return load_method(self.sources, 'serial', {})
