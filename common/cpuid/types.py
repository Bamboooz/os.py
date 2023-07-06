# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# Resource: https://wiki.osdev.org/CPUID

CPUID_VENDOR_AMD             = "AuthenticAMD"
CPUID_VENDOR_AMD_OLD         = "AMDisbetter!" # Early engineering samples of AMD K5 processor
CPUID_VENDOR_INTEL           = "GenuineIntel"
CPUID_VENDOR_VIA             = "VIA VIA VIA "
CPUID_VENDOR_TRANSMETA       = "GenuineTMx86"
CPUID_VENDOR_TRANSMETA_OLD   = "TransmetaCPU"
CPUID_VENDOR_CYRIX           = "CyrixInstead"
CPUID_VENDOR_CENTAUR         = "CentaurHauls"
CPUID_VENDOR_NEXGEN          = "NexGenDriven"
CPUID_VENDOR_UMC             = "UMC UMC UMC "
CPUID_VENDOR_SIS             = "SiS SiS SiS "
CPUID_VENDOR_NSC             = "Geode by NSC"
CPUID_VENDOR_RISE            = "RiseRiseRise"
CPUID_VENDOR_VORTEX          = "Vortex86 SoC"
CPUID_VENDOR_AO486           = "MiSTer AO486"
CPUID_VENDOR_AO486_OLD       = "GenuineAO486"
CPUID_VENDOR_ZHAOXIN         = "  Shanghai  "
CPUID_VENDOR_HYGON           = "HygonGenuine"
CPUID_VENDOR_ELBRUS          = "E2K MACHINE "

CPU_VENDOR_AMD               = "AMD"
CPU_VENDOR_INTEL             = "Intel"
CPU_VENDOR_VIA               = "VIA Technologies"
CPU_VENDOR_TRANSMETA         = "Transmeta"
CPU_VENDOR_CYRIX             = "Cyrix"
CPU_VENDOR_CENTAUR           = "Centaur Technology"
CPU_VENDOR_NEXGEN            = "NexGen"
CPU_VENDOR_UMC               = "United Microelectronics Corporation"
CPU_VENDOR_SIS               = "Silicon Integrated Systems"
CPU_VENDOR_NSC               = "National Semiconductor"
CPU_VENDOR_RISE              = "Rise Technology"
CPU_VENDOR_VORTEX            = "Vortex86 SoC"
CPU_VENDOR_AO486             = "MiSTer AO486"
CPU_VENDOR_ZHAOXIN           = "Zhaoxin Semiconductor"
CPU_VENDOR_HYGON             = "Hygon"
CPU_VENDOR_ELBRUS            = "Elbrus"

# Vendor strings from hypervisors.

CPUID_VENDOR_QEMU            = "TCGTCGTCGTCG"
CPUID_VENDOR_KVM             = " KVMKVMKVM  "
CPUID_VENDOR_VMWARE          = "VMwareVMware"
CPUID_VENDOR_VIRTUALBOX      = "VBoxVBoxVBox"
CPUID_VENDOR_XEN             = "XenVMMXenVMM"
CPUID_VENDOR_HYPERV          = "Microsoft Hv"
CPUID_VENDOR_PARALLELS       = " prl hyperv "
CPUID_VENDOR_PARALLELS_ALT   = " lrpepyh vr " # Sometimes Parallels incorrectly encodes "prl hyperv" as "lrpepyh vr" due to an endianness mismatch.
CPUID_VENDOR_BHYVE           = "bhyve bhyve "
CPUID_VENDOR_QNX             = " QNXQVMBSQG "

HYPERVISOR_VENDOR_QEMU       = "QEMU"
HYPERVISOR_VENDOR_KVM        = "KVM"
HYPERVISOR_VENDOR_VMWARE     = "VMware"
HYPERVISOR_VENDOR_VIRTUALBOX = "VirtualBox"
HYPERVISOR_VENDOR_XEN        = "Xen"
HYPERVISOR_VENDOR_HYPERV     = "Hyper-V"
HYPERVISOR_VENDOR_PARALLELS  = "Parallels"
HYPERVISOR_VENDOR_BHYVE      = "bhyve"
HYPERVISOR_VENDOR_QNX        = "QNX"

TYPE_CPU                     = "CPU"
TYPE_HYPERVISOR              = "Hypervisor"

vendor_map = {
    CPUID_VENDOR_AMD: [CPU_VENDOR_AMD, TYPE_CPU],
    CPUID_VENDOR_AMD_OLD: [CPU_VENDOR_AMD, TYPE_CPU],
    CPUID_VENDOR_INTEL: [CPU_VENDOR_INTEL, TYPE_CPU],
    CPUID_VENDOR_VIA: [CPU_VENDOR_VIA, TYPE_CPU],
    CPUID_VENDOR_TRANSMETA: [CPU_VENDOR_TRANSMETA, TYPE_CPU],
    CPUID_VENDOR_TRANSMETA_OLD: [CPU_VENDOR_TRANSMETA, TYPE_CPU],
    CPUID_VENDOR_CYRIX: [CPU_VENDOR_CYRIX, TYPE_CPU],
    CPUID_VENDOR_CENTAUR: [CPU_VENDOR_CENTAUR, TYPE_CPU],
    CPUID_VENDOR_NEXGEN: [CPU_VENDOR_NEXGEN, TYPE_CPU],
    CPUID_VENDOR_UMC: [CPU_VENDOR_UMC, TYPE_CPU],
    CPUID_VENDOR_SIS: [CPU_VENDOR_SIS, TYPE_CPU],
    CPUID_VENDOR_NSC: [CPU_VENDOR_NSC, TYPE_CPU],
    CPUID_VENDOR_RISE: [CPU_VENDOR_RISE, TYPE_CPU],
    CPUID_VENDOR_VORTEX: [CPU_VENDOR_VORTEX, TYPE_CPU],
    CPUID_VENDOR_AO486: [CPU_VENDOR_AO486, TYPE_CPU],
    CPUID_VENDOR_AO486_OLD: [CPU_VENDOR_AO486, TYPE_CPU],
    CPUID_VENDOR_ZHAOXIN: [CPU_VENDOR_ZHAOXIN, TYPE_CPU],
    CPUID_VENDOR_HYGON: [CPU_VENDOR_HYGON, TYPE_CPU],
    CPUID_VENDOR_ELBRUS: [CPU_VENDOR_ELBRUS, TYPE_CPU],
    CPUID_VENDOR_QEMU: [HYPERVISOR_VENDOR_QEMU, TYPE_HYPERVISOR],
    CPUID_VENDOR_KVM: [HYPERVISOR_VENDOR_KVM, TYPE_HYPERVISOR],
    CPUID_VENDOR_VMWARE: [HYPERVISOR_VENDOR_VMWARE, TYPE_HYPERVISOR],
    CPUID_VENDOR_VIRTUALBOX: [HYPERVISOR_VENDOR_VIRTUALBOX, TYPE_HYPERVISOR],
    CPUID_VENDOR_XEN: [HYPERVISOR_VENDOR_XEN, TYPE_HYPERVISOR],
    CPUID_VENDOR_HYPERV: [HYPERVISOR_VENDOR_HYPERV, TYPE_HYPERVISOR],
    CPUID_VENDOR_PARALLELS: [HYPERVISOR_VENDOR_PARALLELS, TYPE_HYPERVISOR],
    CPUID_VENDOR_PARALLELS_ALT: [HYPERVISOR_VENDOR_PARALLELS, TYPE_HYPERVISOR],
    CPUID_VENDOR_BHYVE: [HYPERVISOR_VENDOR_BHYVE, TYPE_HYPERVISOR],
    CPUID_VENDOR_QNX: [HYPERVISOR_VENDOR_QNX, TYPE_HYPERVISOR]
}

WMIC_CPU_MODEL = 'wmic cpu get name'
WMIC_CPU_CORES = 'wmic cpu get NumberOfLogicalProcessors'
WMIC_CPU_CLOCKSPEED = 'wmic cpu get maxclockspeed'
WMIC_CPU_ARCHITECTURE = 'wmic cpu get Architecture'
WMIC_CPU_VENDOR_ID = 'wmic cpu get manufacturer'

architectures = {
    0: "x86",
    5: "ARM",
    6: "Intel Itanium-based",
    9: "AMD64",
    10: "DEC Alpha",
    12: "ARM64",
    13: "MIPS",
    14: "MIPS64",
    15: "Power PC",
    16: "Power PC64",
    17: "SPARC",
    18: "SPARC64",
    20: "SHx",
    21: "SCx"
}
