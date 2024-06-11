from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='inkpot',
    version='2.2.6',
    description='a small simple library for generating documentation from docstrings',
    url='https://github.com/AxelGard/inkpot',
    author='Axel Gard',
    author_email='axel.gard@tutanota.com',
    license='MIT',
    packages=['inkpot'],
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
    ],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
