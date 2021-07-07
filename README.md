# inkpot
A small simple library for generating documentation from docstrings

inkpot is available on [pip](https://pypi.org/project/inkpot/). **Please give it a star if you like it!**

<img src="https://cdn.pixabay.com/photo/2014/04/05/12/20/ink-316909_960_720.jpg" alt="drawing" width="300"/>

![GitHub stars](https://img.shields.io/github/stars/AxelGard/inkpot?style=social)
![GitHub forks](https://img.shields.io/github/forks/AxelGard/inkpot?style=social)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/Axel_Gard)

![GitHub](https://img.shields.io/github/license/AxelGard/inkpot?style=plastic)
![PyPI](https://img.shields.io/pypi/v/inkpot)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/inkpot)
![PyPI - Downloads](https://img.shields.io/pypi/dm/inkpot)

To know more about way I started this project checkout this **[blog post](https://axelgard.github.io/blog/inkpot/2021/07/01/inkpot-init.html)**

## Installation
```bash
pip install inkpot
```

## Usage
single file
```bash
python3 -m inkpot myfile.py
```
or directory
```bash
python3 -m inkpot myproject/
```
output to a file (also works with directories)
```bash
python3 -m inkpot myfile.py > doc.md
python3 -m inkpot myproject/ > doc.md
```

More functionality and better formatting might be added.

## Example

Python file `tests/.ex/add.py`
```python
def add(a,b):
    """ add to objects """
    return a + b

```

```bash
python3 -m inkpot add.py
```
returns markdown
```
# ex/add.py
## ex/add.py
**def add(a, b)** \
`add to objects `
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details
