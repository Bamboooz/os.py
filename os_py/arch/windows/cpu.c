#include <cpuid.h>  // GCC-provided
#include <stdio.h>
#include <stdint.h>


const char * cpuModel() {
    uint32_t brand[12];

    __get_cpuid(0x80000002, brand+0x0, brand+0x1, brand+0x2, brand+0x3);
    __get_cpuid(0x80000003, brand+0x4, brand+0x5, brand+0x6, brand+0x7);
    __get_cpuid(0x80000004, brand+0x8, brand+0x9, brand+0xa, brand+0xb);

    printf("%s\n", brand);
}
