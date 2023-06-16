/*
Copyright (c) 2022, Bamboooz
All rights reserved.
Use of this source code is governed by a BSD-style license that can be
found in the LICENSE file.
*/

#include <cpuid.h>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <windows.h>
#include <unordered_map>

using namespace std;

static const unordered_map<string, string> vendor_map = {
    { "AMDisbetter!", "AMD" },
    { "AuthenticAMD", "AMD" },
    { "CentaurHauls", "IDT" },
    { "CyrixInstead", "Cyrix" },
    { "GenuineIntel", "Intel" },
    { "TransmetaCPU", "Transmeta" },
    { "GenuineTMx86", "Transmeta" },
    { "Geode by NSC", "National Semiconductor" },
    { "NexGenDriven", "NexGen" },
    { "RiseRiseRise", "Rise" },
    { "SiS SiS SiS", "SiS" },
    { "UMC UMC UMC", "UMC" },
    { "VIA VIA VIA", "VIA" },
    { "Vortex86 SoC", "DM&P Vortex86" },
    { "  Shanghai  ", "Zhaoxin" },
    { "HygonGenuine", "Hygon" },
    { "Genuine  RDC", "RDC Semiconductor Co. Ltd." },
    { "E2K MACHINE", "MCST Elbrus" },
};

const string model() {
    uint32_t cpuid_values[12];

    __get_cpuid(0x80000002, cpuid_values + 0x0, cpuid_values + 0x1, cpuid_values + 0x2, cpuid_values + 0x3);
    __get_cpuid(0x80000003, cpuid_values + 0x4, cpuid_values + 0x5, cpuid_values + 0x6, cpuid_values + 0x7);
    __get_cpuid(0x80000004, cpuid_values + 0x8, cpuid_values + 0x9, cpuid_values + 0xa, cpuid_values + 0xb);

    string brand(reinterpret_cast<char*>(cpuid_values), sizeof(cpuid_values));
    return brand;
}

// I couldn't find a reliable way to get cpu architecture using CPUID, other 2 methods will be used (i will try harder to find them later)

const int cores() {
    uint32_t output[4];
    __cpuid(0x00000001, output[0], output[1], output[2], output[3]);
    return (output[1] >> 16) & 0xFF; // Bits 23-16 of EBX contain the number of cores per processor
}

// I couldn't find a reliable way to get cpu clockspeed using CPUID, other 2 methods will be used (i will try harder to find them later)

const string vendor() {
    uint32_t output[4];

    // Get vendor string from CPUID function 0
    __cpuid(0x00000000, output[0], output[1], output[2], output[3]);

    string vendor;
    vendor.append(reinterpret_cast<char*>(&output[1]), sizeof(uint32_t));
    vendor.append(reinterpret_cast<char*>(&output[3]), sizeof(uint32_t));
    vendor.append(reinterpret_cast<char*>(&output[2]), sizeof(uint32_t));

    return vendor;
}

const string manufacturer() {
    const string s_vendor = vendor();
    auto it = vendor_map.find(s_vendor);
    return it != vendor_map.end() ? it->second : "Unknown";
}
