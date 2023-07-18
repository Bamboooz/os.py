class ospylib_data:
    def __init__(self, **kwargs):
        self._attributes = {name: value for name, value in kwargs.items()}

    def __getattr__(self, name):
        if name not in self._attributes:
            raise AttributeError(f"Requested object '{name}' does not exist.")

        return self._attributes[name]()

    def __setattr__(self, name, value):
        if name not in ["_attributes"]:
            raise AttributeError("Cannot set attribute value on 'ospylib_data'")

        super().__setattr__(name, value)
