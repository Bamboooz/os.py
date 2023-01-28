from os_py import system


# goal: create a program that will retrieve some system information for us

class os_info:
    def __init__(self):
        """
            This is some random function that retrieves some system information for us :D
        """

        print("Operating system: " + system.os_name())
        print("Operating system's release: " + system.os_release())
        print("Operating system version: " + system.os_version())
        print("Operating system platform: " + system.os_platform())
        print("Operating system architecture: " + system.os_architecture())


if __name__ == '__main__':
    os_info()

# Example output:
# Operating system: Windows
# Operating system's release: 10
# Operating system version: 19044
# Operating system platform: Windows-10-10.0.19044-SP0
# Operating system architecture: AMD64
