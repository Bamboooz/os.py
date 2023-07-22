# Copyright (c) 2022, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

class ospylib_data_format:
    """
    Custom way to represent output of ospylib functions, works similarly to namedtuple while having an enhanced speed.
    collections.namedtuple executes all functions returned from the namedtuple but still returns only the one you need.
    ospylib_data_format only executes the function you are getting, and only if you do not specify what are you getting it will execute all functions and return them as a dict.

    def a():
        print('a')
        return 'a'
        
    def b():
        print('b')
        return 'b'

    def from_namedtuple():
        nmtple = namedtuple("nmtple", ["a", "b"])
        return nmtple(a=a(), b=b())

    print(from_namedtuple().a) # prints 'a', 'b' and 'a' instead of only printing 'a' 2 times

    def from_ospylib_data_format():
        ospylibdf = ospylib_data_format(a=a, b=b)
        return ospylibdf

    print(from_ospylib_data_format().a) # prints 'a' 2 times as requested enhancing the code speed by 2x in this example
    """
    def __init__(self, format_name, func_args):
        self._format_name = format_name
        self._attributes = {name: value for name, value in zip(func_args, [None] * len(func_args))}

    def __call__(self, **kwargs):
        for name, value in kwargs.items():
            if name not in self._attributes:
                raise AttributeError(f"Invalid attribute '{name}' for {self._format_name}")

            self._attributes[name] = value

        return self

    def __getattr__(self, name):
        if name not in self._attributes:
            raise AttributeError(f"Requested object '{name}' does not exist.")

        function = self._attributes[name]

        if type(function) is list:
            func, args = tuple(function)
            return func(*args)

        return function() if callable(function) else function

    def __setattr__(self, name, value):
        if name in ["_format_name", "_attributes"]:
            super().__setattr__(name, value)
        else:
            if name not in self._attributes:
                raise AttributeError(f"Invalid attribute '{name}' for {self._format_name}")

            self._attributes[name] = value

    def __str__(self):
        format_name = self._format_name
        container = [f"{format_name}("]

        for attribute, value in self._attributes.items():
            if type(value) is list:
                func, args = tuple(value)
                container.append(f"{attribute}={func(*args)}, ")
                continue

            if callable(value):
                container.append(f"{attribute}={value()}, ")
                continue

            container.append(f"{attribute}={value}, ")

        container = "".join(container)[:-2] + ")"
        return container
