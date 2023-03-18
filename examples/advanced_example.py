import tkinter as tk

from os_py import system, machine


# goal: create tkinter (built-in python graphics library) window that will display some device information to us


class tkinter_sys_info:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced os.py usage example within tkinter window")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.add_main_labels()
        self.add_info_labels()

        self.root.mainloop()

    def add_main_labels(self):
        label1 = tk.Label(self.root, text="System Information:", font=20, fg="black")
        label1.place(x=10, y=10)

        label2 = tk.Label(self.root, text="Network Information:", font=20, fg="black")
        label2.place(x=10, y=200)

        label3 = tk.Label(self.root, text="Machine information:", font=20, fg="black")
        label3.place(x=10, y=380)

    def add_info_labels(self):
        # system information labels
        label1 = tk.Label(self.root, text="Operating system name: " + system.os_name(), font=10, fg="black")
        label1.place(x=30, y=50)

        label2 = tk.Label(self.root, text="Operating system version: " + system.os_version(), font=10, fg="black")
        label2.place(x=30, y=86)

        label3 = tk.Label(self.root, text="Operating system release: " + system.os_release(), font=10, fg="black")
        label3.place(x=30, y=122)

        label4 = tk.Label(self.root, text="Operating system architecture: " + system.os_architecture(), font=10,
                          fg="black")
        label4.place(x=30, y=160)

        # machine information labels
        label9 = tk.Label(self.root, text="Machine name: " + machine.machine_name(), font=10, fg="black")
        label9.place(x=30, y=420)

        label10 = tk.Label(self.root, text="Boot type: " + machine.boot_type(), font=10, fg="black")
        label10.place(x=30, y=460)


if __name__ == '__main__':
    tkinter_sys_info()
