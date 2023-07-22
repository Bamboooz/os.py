# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform
import importlib

from typing import Callable


def load_method(methods, function, not_found):
    for source in methods:
        try:
            product = getattr(source(), function)()
            if product:
                return product
        except Exception:
            continue

    return not_found


def import_by_os(windows, linux, function) -> Callable:
    """
    Imports a function from different code files based on the running operating system.
    """
    os_name = platform.system()
    module_name = windows if os_name == 'Windows' else linux
    imported_module = importlib.import_module(module_name)
    fn = getattr(imported_module, function)
    globals()[function] = fn
    return fn
