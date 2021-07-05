"""
class instance for one file
"""

import ast

from itertools import groupby
from os.path import basename, splitext
from tabulate import tabulate


class File:
    """ File is for interacting with a singel file """

    NODE_TYPES = {ast.Module: 'module',
                  ast.ClassDef: 'class',
                  ast.FunctionDef: 'def',
                  ast.AsyncFunctionDef: 'async-def'
                  }

    def __init__(self, path: str, module: str = '<string>'):
        """ constructor """
        self._path = path
        self.module = module
        self.grouped = None

    def _get_docstrings(self, source):
        tree = ast.parse(source)

        for node in ast.walk(tree):
            if isinstance(node, tuple(File.NODE_TYPES)):
                docstring = ast.get_docstring(node)
                lineno = getattr(node, 'lineno', None)

                if (node.body and isinstance(node.body[0], ast.Expr) and
                        isinstance(node.body[0].value, ast.Str)):

                    lineno = node.body[0].lineno - \
                        len(node.body[0].value.s.splitlines()) + 1

                yield (node, getattr(node, 'name', None), lineno, docstring)

    def filter(self):
        """ find node-types and docstrings in the file """
        # Source: https://gist.github.com/SpotlightKid/1548cb6c97f2a844f72d
        with open(self._path) as source:
            if hasattr(source, 'read'):
                filename = getattr(source, 'name', self.module)
                self.module = splitext(basename(filename))[0]
                source = source.read()

            docstrings = sorted(self._get_docstrings(source),
                                key=lambda x: (File.NODE_TYPES.get(type(x[0])), x[1]))
            self.grouped = groupby(
                docstrings, key=lambda x: File.NODE_TYPES.get(type(x[0])))

    def output(self):
        """ outputs all node-types and their respective docstrings """
        if not self.grouped:
            self.filter()

        head = ["type", "name", "doc-str"]
        table = []

        for type_, group in self.grouped:
            for node, name, lineno, docstring in group:
                name = name if name else self.module
                table.append([str(type_), str(name), str(docstring).strip()])

        # Use pipe for markdown files
        print("## %s" % (self._path))
        print(tabulate(table, headers=head, tablefmt="pipe"))
        print('\n')
