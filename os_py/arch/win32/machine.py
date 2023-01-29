import subprocess

from scripts.err import Errors


def boot_type():
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
        Errors().no_permission()
