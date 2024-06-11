import subprocess
import pathlib


def test_integration_simple_file():
    test_dir = pathlib.Path().resolve()
    file_to_parse = './tests/.ex/add.py'
    command = ['python3', '-m', 'inkpot', file_to_parse]
    result = subprocess.check_output(command, cwd=test_dir, text=True)
    expected = "# ./tests/.ex/add.py\n## ./tests/.ex/add.py\n**def add(a, b)** \\\n`add to objects ` \n\n\n"
    assert result == expected, f"Failed to parse {file_to_parse}"


def test_integration_type_anotations():
    test_dir = pathlib.Path().resolve()
    file_to_parse = './tests/.ex/typed.py'
    command = ['python3', '-m', 'inkpot', file_to_parse]
    result = subprocess.check_output(command, cwd=test_dir, text=True)
    expected = '# ./tests/.ex/typed.py\n## ./tests/.ex/typed.py\n**def add_one(x: int) -> int** \\\n`None` \n\n\n'
    assert result == expected, f"Failed to parse {file_to_parse}"


def test_integration_classes():
    test_dir = pathlib.Path().resolve()
    file_to_parse = './tests/.ex/car.py'
    command = ['python3', '-m', 'inkpot', file_to_parse]
    result = subprocess.check_output(command, cwd=test_dir, text=True)
    expected = '# ./tests/.ex/car.py\n## ./tests/.ex/car.py\n### class Car()\n`The Car class` \n\n> ### class Engine()\n> `The Engine subclass` \n>\n>> **def \\_\\_init\\_\\_(self)** \\\n>> `None` \n>>\n> **def \\_\\_init\\_\\_(self)** \\\n> `None` \n>\n> **def start(self, time: str, car_key)** \\\n> `starts the engine of the car` \n>\n> **def stop(self, a=1, b=2, c=None, \\*args, \\*\\*kwargs)** \\\n> `Stop the engine of the car!` \n>\n> **def honk(self)** \\\n> `Use` \\\n`"the"` \\\n`""horn""` \n>\n>> **def nested_test()** \\\n>> `nested function inside honk` \n>>\n> **def \\_\\_str\\_\\_(self)** \\\n> `Example of a longer multiline-docstring,` \\\n`everything will still be formatted correctly` \n>\n> **@staticmethod \\\n@staticmethod \\\ndef funcname(param1: str, param2: int)** \\\n> `The docstring to the static method` \n>\n**async def async_def_test(a, b, c)** \\\n`Testing coroutines declared with async syntax` \n\n**def no_class_def_test()** \\\n`None` \n\n\n' 
    assert result == expected, f"Failed to parse {file_to_parse}"


def test_integration_dir():
    test_dir = pathlib.Path().resolve()
    file_to_parse = './tests/.ex/dir/'
    command = ['python3', '-m', 'inkpot', file_to_parse]
    result = subprocess.check_output(command, cwd=test_dir, text=True)
    expected = '# ./tests/.ex/dir/\n## ./tests/.ex/dir/point.py\n### class Point()\n`Creates a point on a coordinate plane with values x and y.` \n\n> **def \\_\\_init\\_\\_(self, x_init, y_init)** \\\n> `Defines x and y variables` \n>\n> **def shift(self, x, y)** \\\n> `Determines where x and y move` \n>\n> **def \\_\\_repr\\_\\_(self)** \\\n> `None` \n>\n\n## ./tests/.ex/dir/sub_dir/foo.py\n**def inverse_sqrt(x: int)** \\\n`a normal inverse square root ` \n\n\n'
    assert result == expected, f"Failed to parse {file_to_parse}"


#print(repr(result))