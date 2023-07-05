/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#ifdef _WIN32
    #include "arch/windows/gpu.c"
    #include "arch/windows/mem.c"
    #include "arch/windows/swap.c"
    #include "arch/windows/cpu.c"
#elif __linux__
    #include "arch/linux/gpu.c"
    #include "arch/linux/mem.c"
    #include "arch/linux/swap.c"
    #include "arch/linux/cpu.c"
#endif
