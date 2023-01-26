import re


def bios_type():
    with open(r'C:\Windows\Panther\setupact.log') as f:
        pattern = re.compile(r'Detected boot environment: (\w+)')
        for line in f:
            match = pattern.search(line)
            if match:
                boot_type = match.group(1).upper()
                if boot_type == 'EFI':
                    return 'UEFI'
                else:
                    return 'BIOS'
