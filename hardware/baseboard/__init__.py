# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from common.data import ospylib_data_format
from common.load import import_by_os


def hw_baseboard() -> ospylib_data_format:
    """
    Returns a namedtuple-like object containing a variety of system information.

    :returns:
        - product: Returns the motherboard's product
        - manufacturer: Returns the motherboard's manufacturer
        - version: Returns the motherboard's version
    """
    product = import_by_os(windows="arch.windows.baseboard", linux="arch.linux.baseboard", function="product")
    manufacturer = import_by_os(windows="arch.windows.baseboard", linux="arch.linux.baseboard", function="manufacturer")
    version = import_by_os(windows="arch.windows.baseboard", linux="arch.linux.baseboard", function="version")

    return ospylib_data_format(product=product, manufacturer=manufacturer, version=version)
