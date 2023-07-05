# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from display.arch.windows.nvidia.graphics import m_used, m_total


def usage(num) -> float:
    mem_used = m_used(num)
    mem_total = m_total(num)
    return (mem_used / mem_total) * 100
