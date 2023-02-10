import subprocess


def linux_ram_amount():
    output = subprocess.getoutput('free').strip()
    output = output.split('\n')[1:]
    output.pop()
    output = output[0].replace('Mem:', '').strip().split(' ')

    return str(round(int(output[0])/1024**2)) + 'GB'
