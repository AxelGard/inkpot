"""
class instance for one file
"""

import ast

from os.path import basename, splitext
from tabulate import tabulate


class File:
    """ File is for interacting with a singel file """

    NODE_TYPES = {ast.ClassDef: 'class',
                  ast.FunctionDef: 'def',
                  ast.AsyncFunctionDef: 'async-def'
                  }

    def __init__(self, path: str):
        """ constructor """
        self._path = path
        self.nodes = {}

    def filter(self, module: str = '<string>'):
        """ find node-types and docstrings in the file """
        with open(self._path) as source:
            if hasattr(source, 'read'):
                filename = getattr(source, 'name', module)
                module = splitext(basename(filename))[0]
                source = source.read()

                tree = ast.parse(source)

                for node in ast.walk(tree):
                    # Classes
                    if isinstance(node, ast.ClassDef):
                        # FIXME: Maybe add inheritance support: node.bases[0].id
                        for child in node.body:
                            # Class methods
                            if isinstance(child, ast.FunctionDef) or \
                                    isinstance(child, ast.AsyncFunctionDef):
                                child.parent = node
                            # Nested class support
                            if isinstance(child, ast.ClassDef):
                                child.parent = node
                    # Functions
                    if isinstance(node, ast.FunctionDef) or \
                            isinstance(node, ast.AsyncFunctionDef):
                        for child in node.body:
                            # Nested function support
                            if isinstance(child, ast.FunctionDef):
                                child.parent = node

                    if isinstance(node, tuple(File.NODE_TYPES)):
                        if hasattr(node, 'name'):
                            self.nodes[str(node.name)] = node

    def output(self):
        """ outputs all node-types and their respective docstrings """

        head = ["type", "name", "doc-str"]
        table = []

        # Use pipe for markdown files
        print("## %s" % (self._path))
        # print(tabulate(table, headers=head, tablefmt="pipe"))

        for node in self.nodes.values():
            print('Type:', File.NODE_TYPES.get(type(node)))
            print('Name:', node.name)
            if hasattr(node, 'parent'):
                print('Parent:', node.parent.name)
            print(ast.get_docstring(node))
            print('')
        print('')
