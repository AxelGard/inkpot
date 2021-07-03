class car:
    def __init__(self):
        self.wheels = 0
        self.doors = 0
        self.engine = ""
        self.number_plate = ""

    def start(self):
        """starts the engine of the car"""
        self.engine = """Running"""

    def stop(self):
        """Stop the engine of the car!"""
        self.engine = "Stopping"

    def honk(self):
        """
        Use
        "The"
        ""Horn""
        """
        print("Honking...")
        print("Honk Honk!")

    def __str__(self):
        """
        example of a longer multiline-docstring,
        everything will be printed on a single line
        """
        return self.number_plate
