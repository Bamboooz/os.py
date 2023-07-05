/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#ifdef _WIN32
    #include "arch/windows/swap.c"
#elif __linux__
    #include "arch/linux/swap.c"
#endif
