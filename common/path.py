# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import system


def drive_to_path(drive) -> str:
    """
    Windows: Converts drive letters to root paths ("C" -> "C:\\", "C:\\" -> "C:\\") etc.
    Linux: Converts drive letters to root paths ("dev" -> "/dev") etc.
    """
    if system.name() == 'Windows':
        return (drive.strip().upper().rstrip("\\") + "\\") if len(drive.strip()) > 1 else drive.strip().upper() + ":\\"
    elif system.name() == 'Linux':
        return drive if drive.startswith('/') else f'/{drive}'
