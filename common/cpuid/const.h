/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

// Resource : https://wiki.osdev.org/CPUID

#include "../types/dict.h"

#define CPUID_VENDOR_AMD             "AuthenticAMD"
#define CPUID_VENDOR_AMD_OLD         "AMDisbetter!" // Early engineering samples of AMD K5 processor
#define CPUID_VENDOR_INTEL           "GenuineIntel"
#define CPUID_VENDOR_VIA             "VIA VIA VIA "
#define CPUID_VENDOR_TRANSMETA       "GenuineTMx86"
#define CPUID_VENDOR_TRANSMETA_OLD   "TransmetaCPU"
#define CPUID_VENDOR_CYRIX           "CyrixInstead"
#define CPUID_VENDOR_CENTAUR         "CentaurHauls"
#define CPUID_VENDOR_NEXGEN          "NexGenDriven"
#define CPUID_VENDOR_UMC             "UMC UMC UMC "
#define CPUID_VENDOR_SIS             "SiS SiS SiS "
#define CPUID_VENDOR_NSC             "Geode by NSC"
#define CPUID_VENDOR_RISE            "RiseRiseRise"
#define CPUID_VENDOR_VORTEX          "Vortex86 SoC"
#define CPUID_VENDOR_AO486           "MiSTer AO486"
#define CPUID_VENDOR_AO486_OLD       "GenuineAO486"
#define CPUID_VENDOR_ZHAOXIN         "  Shanghai  "
#define CPUID_VENDOR_HYGON           "HygonGenuine"
#define CPUID_VENDOR_ELBRUS          "E2K MACHINE "
 
#define CPU_VENDOR_AMD               "AMD"
#define CPU_VENDOR_INTEL             "Intel"
#define CPU_VENDOR_VIA               "VIA Technologies"
#define CPU_VENDOR_TRANSMETA         "Transmeta"
#define CPU_VENDOR_CYRIX             "Cyrix"
#define CPU_VENDOR_CENTAUR           "Centaur Technology"
#define CPU_VENDOR_NEXGEN            "NexGen"
#define CPU_VENDOR_UMC               "United Microelectronics Corporation"
#define CPU_VENDOR_SIS               "Silicon Integrated Systems"
#define CPU_VENDOR_NSC               "National Semiconductor"
#define CPU_VENDOR_RISE              "Rise Technology"
#define CPU_VENDOR_VORTEX            "Vortex86 SoC"
#define CPU_VENDOR_AO486             "MiSTer AO486"
#define CPU_VENDOR_ZHAOXIN           "Zhaoxin Semiconductor"
#define CPU_VENDOR_HYGON             "Hygon"
#define CPU_VENDOR_ELBRUS            "Elbrus"

// Vendor strings from hypervisors.
#define CPUID_VENDOR_QEMU            "TCGTCGTCGTCG"
#define CPUID_VENDOR_KVM             " KVMKVMKVM  "
#define CPUID_VENDOR_VMWARE          "VMwareVMware"
#define CPUID_VENDOR_VIRTUALBOX      "VBoxVBoxVBox"
#define CPUID_VENDOR_XEN             "XenVMMXenVMM"
#define CPUID_VENDOR_HYPERV          "Microsoft Hv"
#define CPUID_VENDOR_PARALLELS       " prl hyperv "
#define CPUID_VENDOR_PARALLELS_ALT   " lrpepyh vr " // Sometimes Parallels incorrectly encodes "prl hyperv" as "lrpepyh vr" due to an endianness mismatch.
#define CPUID_VENDOR_BHYVE           "bhyve bhyve "
#define CPUID_VENDOR_QNX             " QNXQVMBSQG "

#define HYPERVISOR_VENDOR_QEMU       "QEMU"
#define HYPERVISOR_VENDOR_KVM        "KVM"
#define HYPERVISOR_VENDOR_VMWARE     "VMware"
#define HYPERVISOR_VENDOR_VIRTUALBOX "VirtualBox"
#define HYPERVISOR_VENDOR_XEN        "Xen"
#define HYPERVISOR_VENDOR_HYPERV     "Hyper-V"
#define HYPERVISOR_VENDOR_PARALLELS  "Parallels"
#define HYPERVISOR_VENDOR_BHYVE      "bhyve"
#define HYPERVISOR_VENDOR_QNX        "QNX"

#define TYPE_CPU                     "CPU"
#define TYPE_HYPERVISOR              "Hypervisor"

dict vmap_manufacturer[] = {
    { CPUID_VENDOR_AMD,           CPU_VENDOR_AMD },
    { CPUID_VENDOR_AMD_OLD,       CPU_VENDOR_AMD },
    { CPUID_VENDOR_INTEL,         CPU_VENDOR_INTEL },
    { CPUID_VENDOR_VIA,           CPU_VENDOR_VIA },
    { CPUID_VENDOR_TRANSMETA,     CPU_VENDOR_TRANSMETA },
    { CPUID_VENDOR_TRANSMETA_OLD, CPU_VENDOR_TRANSMETA },
    { CPUID_VENDOR_CYRIX,         CPU_VENDOR_CYRIX },
    { CPUID_VENDOR_CENTAUR,       CPU_VENDOR_CENTAUR },
    { CPUID_VENDOR_NEXGEN,        CPU_VENDOR_NEXGEN },
    { CPUID_VENDOR_UMC,           CPU_VENDOR_UMC },
    { CPUID_VENDOR_SIS,           CPU_VENDOR_SIS },
    { CPUID_VENDOR_NSC,           CPU_VENDOR_NSC },
    { CPUID_VENDOR_RISE,          CPU_VENDOR_RISE },
    { CPUID_VENDOR_VORTEX,        CPU_VENDOR_VORTEX },
    { CPUID_VENDOR_AO486,         CPU_VENDOR_AO486 },
    { CPUID_VENDOR_AO486_OLD,     CPU_VENDOR_AO486 },
    { CPUID_VENDOR_ZHAOXIN,       CPU_VENDOR_ZHAOXIN },
    { CPUID_VENDOR_HYGON,         CPU_VENDOR_HYGON },
    { CPUID_VENDOR_ELBRUS,        CPU_VENDOR_ELBRUS },
    { CPUID_VENDOR_QEMU,          HYPERVISOR_VENDOR_QEMU },
    { CPUID_VENDOR_KVM,           HYPERVISOR_VENDOR_KVM },
    { CPUID_VENDOR_VMWARE,        HYPERVISOR_VENDOR_VMWARE },
    { CPUID_VENDOR_VIRTUALBOX,    HYPERVISOR_VENDOR_VIRTUALBOX },
    { CPUID_VENDOR_XEN,           HYPERVISOR_VENDOR_XEN },
    { CPUID_VENDOR_HYPERV,        HYPERVISOR_VENDOR_HYPERV },
    { CPUID_VENDOR_PARALLELS,     HYPERVISOR_VENDOR_PARALLELS },
    { CPUID_VENDOR_PARALLELS_ALT, HYPERVISOR_VENDOR_PARALLELS },
    { CPUID_VENDOR_BHYVE,         HYPERVISOR_VENDOR_BHYVE },
    { CPUID_VENDOR_QNX,           HYPERVISOR_VENDOR_QNX }
};

dict vmap_type[] = {
    { CPUID_VENDOR_AMD,           TYPE_CPU },
    { CPUID_VENDOR_AMD_OLD,       TYPE_CPU },
    { CPUID_VENDOR_INTEL,         TYPE_CPU },
    { CPUID_VENDOR_VIA,           TYPE_CPU },
    { CPUID_VENDOR_TRANSMETA,     TYPE_CPU },
    { CPUID_VENDOR_TRANSMETA_OLD, TYPE_CPU },
    { CPUID_VENDOR_CYRIX,         TYPE_CPU },
    { CPUID_VENDOR_CENTAUR,       TYPE_CPU },
    { CPUID_VENDOR_NEXGEN,        TYPE_CPU },
    { CPUID_VENDOR_UMC,           TYPE_CPU },
    { CPUID_VENDOR_SIS,           TYPE_CPU },
    { CPUID_VENDOR_NSC,           TYPE_CPU },
    { CPUID_VENDOR_RISE,          TYPE_CPU },
    { CPUID_VENDOR_VORTEX,        TYPE_CPU },
    { CPUID_VENDOR_AO486,         TYPE_CPU },
    { CPUID_VENDOR_AO486_OLD,     TYPE_CPU },
    { CPUID_VENDOR_ZHAOXIN,       TYPE_CPU },
    { CPUID_VENDOR_HYGON,         TYPE_CPU },
    { CPUID_VENDOR_ELBRUS,        TYPE_CPU },
    { CPUID_VENDOR_QEMU,          TYPE_HYPERVISOR },
    { CPUID_VENDOR_KVM,           TYPE_HYPERVISOR },
    { CPUID_VENDOR_VMWARE,        TYPE_HYPERVISOR },
    { CPUID_VENDOR_VIRTUALBOX,    TYPE_HYPERVISOR },
    { CPUID_VENDOR_XEN,           TYPE_HYPERVISOR },
    { CPUID_VENDOR_HYPERV,        TYPE_HYPERVISOR },
    { CPUID_VENDOR_PARALLELS,     TYPE_HYPERVISOR },
    { CPUID_VENDOR_PARALLELS_ALT, TYPE_HYPERVISOR },
    { CPUID_VENDOR_BHYVE,         TYPE_HYPERVISOR },
    { CPUID_VENDOR_QNX,           TYPE_HYPERVISOR }
};

#define FEATURE_CPUID_BUFFER 4

#define ECX 0x0
#define EAX 0x1

enum {
    CPUID_FEAT_ECX_SSE3         = 1 << 0, 
    CPUID_FEAT_ECX_PCLMUL       = 1 << 1,
    CPUID_FEAT_ECX_DTES64       = 1 << 2,
    CPUID_FEAT_ECX_MONITOR      = 1 << 3,  
    CPUID_FEAT_ECX_DS_CPL       = 1 << 4,  
    CPUID_FEAT_ECX_VMX          = 1 << 5,  
    CPUID_FEAT_ECX_SMX          = 1 << 6,  
    CPUID_FEAT_ECX_EST          = 1 << 7,  
    CPUID_FEAT_ECX_TM2          = 1 << 8,  
    CPUID_FEAT_ECX_SSSE3        = 1 << 9,  
    CPUID_FEAT_ECX_CID          = 1 << 10,
    CPUID_FEAT_ECX_SDBG         = 1 << 11,
    CPUID_FEAT_ECX_FMA          = 1 << 12,
    CPUID_FEAT_ECX_CX16         = 1 << 13, 
    CPUID_FEAT_ECX_XTPR         = 1 << 14, 
    CPUID_FEAT_ECX_PDCM         = 1 << 15, 
    CPUID_FEAT_ECX_PCID         = 1 << 17, 
    CPUID_FEAT_ECX_DCA          = 1 << 18, 
    CPUID_FEAT_ECX_SSE4_1       = 1 << 19, 
    CPUID_FEAT_ECX_SSE4_2       = 1 << 20, 
    CPUID_FEAT_ECX_X2APIC       = 1 << 21, 
    CPUID_FEAT_ECX_MOVBE        = 1 << 22, 
    CPUID_FEAT_ECX_POPCNT       = 1 << 23, 
    CPUID_FEAT_ECX_TSC          = 1 << 24, 
    CPUID_FEAT_ECX_AES          = 1 << 25, 
    CPUID_FEAT_ECX_XSAVE        = 1 << 26, 
    CPUID_FEAT_ECX_OSXSAVE      = 1 << 27, 
    CPUID_FEAT_ECX_AVX          = 1 << 28,
    CPUID_FEAT_ECX_F16C         = 1 << 29,
    CPUID_FEAT_ECX_RDRAND       = 1 << 30,

    CPUID_FEAT_EDX_FPU          = 1 << 0,  
    CPUID_FEAT_EDX_VME          = 1 << 1,  
    CPUID_FEAT_EDX_DE           = 1 << 2,  
    CPUID_FEAT_EDX_PSE          = 1 << 3,  
    CPUID_FEAT_EDX_TSC          = 1 << 4,  
    CPUID_FEAT_EDX_MSR          = 1 << 5,  
    CPUID_FEAT_EDX_PAE          = 1 << 6,  
    CPUID_FEAT_EDX_MCE          = 1 << 7,  
    CPUID_FEAT_EDX_CX8          = 1 << 8,  
    CPUID_FEAT_EDX_APIC         = 1 << 9,  
    CPUID_FEAT_EDX_SEP          = 1 << 11, 
    CPUID_FEAT_EDX_MTRR         = 1 << 12, 
    CPUID_FEAT_EDX_PGE          = 1 << 13, 
    CPUID_FEAT_EDX_MCA          = 1 << 14, 
    CPUID_FEAT_EDX_CMOV         = 1 << 15, 
    CPUID_FEAT_EDX_PAT          = 1 << 16, 
    CPUID_FEAT_EDX_PSE36        = 1 << 17, 
    CPUID_FEAT_EDX_PSN          = 1 << 18, 
    CPUID_FEAT_EDX_CLFLUSH      = 1 << 19, 
    CPUID_FEAT_EDX_DS           = 1 << 21, 
    CPUID_FEAT_EDX_ACPI         = 1 << 22, 
    CPUID_FEAT_EDX_MMX          = 1 << 23, 
    CPUID_FEAT_EDX_FXSR         = 1 << 24, 
    CPUID_FEAT_EDX_SSE          = 1 << 25, 
    CPUID_FEAT_EDX_SSE2         = 1 << 26, 
    CPUID_FEAT_EDX_SS           = 1 << 27, 
    CPUID_FEAT_EDX_HTT          = 1 << 28, 
    CPUID_FEAT_EDX_TM           = 1 << 29, 
    CPUID_FEAT_EDX_IA64         = 1 << 30,
    CPUID_FEAT_EDX_PBE          = 1u << 31
};
