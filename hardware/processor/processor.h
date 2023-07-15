/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include "../../common/cpuid/cpuid.c"

#if cpuid_supported 
    #include "shared/processor.c"
#else
    if __linux__
        #include "arch/linux/processor.c"
    #endif
#endif


