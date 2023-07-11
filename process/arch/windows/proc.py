from common.prompt.prompt import execute_command


def running_pids() -> list:
    processes = execute_command("TASKLIST /nh /FO CSV", 0, ['cp1252'])
    pids = [int(process.split(',')[1].replace('"', '')) for process in processes]
    return pids


def running_processes() -> list:
    processes = execute_command("TASKLIST /nh /FO CSV", 0, ['cp1252'])
    pids = [process.split(',')[0].replace('"', '') for process in processes]
    return pids
