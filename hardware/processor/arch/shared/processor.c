/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include "../../../common/cpuid/const.h"
#include "../../../common/cpuid/cpuid.c"
#include "../../../common/strlib.h"

#define MAX_BUFFER_SIZE 1024

char * vendor() {
    unsigned int cpuidResults[4];
    executeCpuid(cpuidResults, 0x0, 0x0);

    char * vendorId = (char*)malloc(13); // 13 is always size for CPU vendor id
    if (vendorId == NULL) {
        return NULL;
    }

    memcpy(vendorId, &(cpuidResults[1]), 4);
    memcpy(vendorId + 4, &(cpuidResults[3]), 4);
    memcpy(vendorId + 8, &(cpuidResults[2]), 4);
    vendorId[12] = '\0';

    return vendorId;
}

char * model() {
    unsigned int cpuidResults[4];

    char * modelName = NULL;
    int modelLength = 0;

    for (unsigned int i = 0x80000002; i <= 0x80000004; ++i) {
        executeCpuid(cpuidResults, i, 0x0);
        char tempModel[17]; // Maximum submodel size is 16 characters + 1 null-terminator
        snprintf(tempModel, sizeof(tempModel), "%s", (char*)cpuidResults);
        modelLength += strlen(tempModel);
        modelName = realloc(modelName, modelLength + 1); // Add 1 for the null-terminator
        strcat(modelName, tempModel);
    }

    return modelName;
}

const char * manufacturer() {
    size_t dict_size = sizeof(vmap_manufacturer) / sizeof(vmap_manufacturer[0]);
    char * manufacturer = value_from_dict(vmap_manufacturer, dict_size, vendor(), "");
    return manufacturer;
}

const char * cpu_type() {
    size_t dict_size = sizeof(vmap_type) / sizeof(vmap_type[0]);
    char * cpu_type = value_from_dict(vmap_type, dict_size, vendor(), "");
    return cpu_type;
}

const int physical_cores() {
    unsigned int cpuidResults[4];
    executeCpuid(cpuidResults, 0x1, 0x0);
    return (cpuidResults[1] >> 8) & 0xFF;
}

const int logical_cores() {
    unsigned int cpuidResults[4];
    executeCpuid(cpuidResults, 0x1, 0x0);
    unsigned int numCores = (cpuidResults[1] >> 16) & 0xFF;
    return numCores;
}

const int hyper_threading_enabled() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_HTT) != 0;
}

int sse3_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SSE3) != 0;
}

int pclmul_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_PCLMUL) != 0;
}

int dtes64_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_DTES64) != 0;
}

int monitor_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_MONITOR) != 0;
}

int ds_cpl_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_DS_CPL) != 0;
}

int vmx_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_VMX) != 0;
}

int smx_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SMX) != 0;
}

int est_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_EST) != 0;
}

int tm2_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_TM2) != 0;
}

int ssse3_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SSSE3) != 0;
}

int cid_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_CID) != 0;
}

int sdbg_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SDBG) != 0;
}

int fma_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_FMA) != 0;
}

int cx16_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_CX16) != 0;
}

int xptr_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_XTPR) != 0;
}

int pdcm_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_PDCM) != 0;
}

int pcid_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_PCID) != 0;
}

int dca_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_DCA) != 0;
}

int sse4_1_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SSE4_1) != 0;
}

int sse4_2_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_SSE4_2) != 0;
}

int x2apic_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_X2APIC) != 0;
}

int movbe_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_MOVBE) != 0;
}

int popcnt_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_POPCNT) != 0;
}

int tsc_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_TSC) != 0;
}

int aes_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_AES) != 0;
}

int xsave_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_XSAVE) != 0;
}

int osxsave_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_OSXSAVE) != 0;
}

int avx_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_AVX) != 0;
}

int f16c_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_F16C) != 0;
}

int rdrand_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[2] & CPUID_FEAT_ECX_RDRAND) != 0;
}

int fpu_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_FPU) != 0;
}

int vme_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_VME) != 0;
}

int de_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_DE) != 0;
}

int pse_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PSE) != 0;
}

int msr_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_MSR) != 0;
}

int pae_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PAE) != 0;
}

int mce_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_MCE) != 0;
}

int cx8_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_CX8) != 0;
}

int apic_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_APIC) != 0;
}

int sep_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_SEP) != 0;
}

int mtrr_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_MTRR) != 0;
}

int pge_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PGE) != 0;
}

int mca_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_MCA) != 0;
}

int cmov_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_CMOV) != 0;
}

int pat_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PAT) != 0;
}

int pse36_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PSE36) != 0;
}

int psn_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PSN) != 0;
}

int clfsh_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_CLFLUSH) != 0;
}

int ds_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_DS) != 0;
}

int acpi_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_ACPI) != 0;
}

int mmx_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_MMX) != 0;
}

int fxsr_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_FXSR) != 0;
}

int sse_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_SSE) != 0;
}

int sse2_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_SSE2) != 0;
}

int ss_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_SS) != 0;
}

int tm_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_TM) != 0;
}

int pbe_supported() {
    unsigned int cpuidResults[FEATURE_CPUID_BUFFER];
    executeCpuid(cpuidResults, EAX, ECX);
    return (cpuidResults[3] & CPUID_FEAT_EDX_PBE) != 0;
}
