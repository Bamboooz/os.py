# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import subprocess
import winreg


def parse_wmic(command):
    """Helper function to parse the output of WMIC commands.

    Args:
        command (str): The WMIC command to execute.

    Returns:
        dict or str: A dictionary containing the data from the output, with each row split into a separate dictionary entry, or the single output value if there's only one item in the dictionary.
    """
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = p.communicate()

    if p.returncode != 0:
        raise subprocess.CalledProcessError(p.returncode, command, error)

    # Decode the output and remove any non-ASCII characters
    output = output.decode('ascii', 'ignore')

    # Split the output into lines, removing the first line (which is the WMIC description)
    lines = output.strip().split('\n')[1:]

    # Split each line into a dictionary entry with the row number as the key
    data = {}
    for i, line in enumerate(lines):
        data[i+1] = {"output": line.strip()}

    return data


def load_winreg_key(winreg_key):
    """Helper function to load a value from a WinReg key.

    Args:
        winreg_key (list): A list containing the WinReg hive, subkey, and value name.

    Returns:
        str: The value of the specified key.
    """
    key = winreg.OpenKey(winreg_key[0], winreg_key[1])
    return winreg.QueryValueEx(key, winreg_key[2])[0]


def read_powershell_command(command):
    """Helper function to parse the output of PowerShell commands.

    Args:
        command (str): The PowerShell command to execute.

    Returns:
        dict: A dictionary containing the data from the output, with each row split into a separate dictionary entry.
    """
    p = subprocess.Popen(["powershell", "-Command", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode != 0:
        raise subprocess.CalledProcessError(p.returncode, command, error)

    # Decode the output and remove any non-ASCII characters
    output = output.decode('ascii', 'ignore')

    if not output.strip():
        return None

    # Split the output into lines
    lines = output.strip().split('\n')

    # Split each line into a dictionary entry with the row number as the key
    data = {}
    for i, line in enumerate(lines):
        data[i+1] = {"output": line.strip()}

    return data
