import sys
from scripts.color import color_codes as col


class Errors:
    @staticmethod
    def print_err(text):
        print(col.RED + text + col.DEFAULT)
        sys.exit(-1)

    @staticmethod
    def print_warn(text):
        print(col.YELLOW + text + col.DEFAULT)

    def unsupported_os(self):
        self.print_err('Error: Unsupported platform.')

    def no_permission(self):
        self.print_err('Error: To get this data you need to run your project with elevated permissions.')

    def no_support(self):
        self.print_err('Error: Your platform does not support this command.')
