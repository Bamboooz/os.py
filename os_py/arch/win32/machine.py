import os.path
import subprocess
import re

from scripts._common import Handler


def boot_type():
    def boot_type_from_setupact():
        with open(r'C:\Windows\Panther\setupact.log') as f:
            pattern = re.compile(r'Detected boot environment: (\w+)')

            # Iterate over every line of file until finds a match
            for line in f:
                match = pattern.search(line)
                if match:
                    # Receives 'BIOS' or 'UEFI'
                    boot_type = match.group(1).upper()
                    return boot_type

    def boot_type_from_bcdedit():
        try:
            out = subprocess.check_output(['bcdedit']).decode('utf-8')

            is_loader = False
            for line in out.split('\n'):
                # Ignore lines until the Windows Boot Loader section
                if not is_loader and 'Windows Boot Loader' in line:
                    is_loader = True

                if not is_loader:
                    continue

                # Ignore lines until the path subsection
                if not line.startswith('path'):
                    continue

                # Receives 'exe' (BIOS) or 'efi' (UEFI)
                boot_type = 'BIOS' if line[-3:] == 'exe' else 'UEFI'
                return boot_type
        except:
            Handler.exception("No administrator permissions")

    if os.path.exists(r'C:\Windows\Panther\setupact.log'):
        return boot_type_from_setupact()
    else:
        return boot_type_from_bcdedit()
