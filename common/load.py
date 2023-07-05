# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import platform
import importlib

from typing import Callable


WINDOWS = 'Windows'
LINUX = 'Linux'


def load_method(methods, function, not_found):
    for source in methods:
        try:
            product = getattr(source(), function)()
            if product is not None and product != "": return product
        except:
            continue

    return not_found


def import_by_os(code_files, function_name) -> Callable:
    """
    Imports a function from different code files based on the running operating system.
    """
    os_name = platform.system()
    module_name = code_files[os_name]
    imported_module = importlib.import_module(module_name)
    function = getattr(imported_module, function_name)
    globals()[function_name] = function
    return function
