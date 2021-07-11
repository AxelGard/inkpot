class Car():
    """The Car class"""
    class Engine:
        """The Engine subclass"""

        def __init__(self):
            self.fuel = 0

    def __init__(self):
        super().__init__(self)
        self.wheels = 0
        self.doors = 0
        self.engine = ""
        self.number_plate = ""

    def start(self, time: str, car_key):
        """starts the engine of the car"""
        self.engine = """Running"""

    def stop(self, a=1, b=2, c=None, *args, **kwargs):  # Comment after line
        """Stop the engine of the car!"""
        self.engine = "Stopping"

    def honk(self):
        """
        Use
        "the"
        ""horn""
        """
        def nested_test():
            "nested function inside honk"
            pass
        # def
        test = "def"
        print("Honking...")
        print("Honk Honk!")

    def __str__(self):
        """
        Eexample of a longer multiline-docstring,
        everything will still be formatted correctly
        """
        return self.number_plate

    @staticmethod
    @staticmethod
    def funcname(parameter_list):
        """
        docstring
        """
        pass


def no_class_def_test():
    pass
