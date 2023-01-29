def boot_type():
    try:
        open("/sys/firmware/efi")
        return 'UEFI'
    except IOError:
        return 'BIOS'
