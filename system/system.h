/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#if _WIN32
    #include "arch/windows/firmware.c"
    #include "arch/windows/sys.c"
#elif __linux__
    #include "arch/linux/firmware.c"
    #include "arch/linux/sys.c"
#endif
