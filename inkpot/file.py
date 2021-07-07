"""
class instance for one file
"""

import ast
from os.path import basename, splitext


class File:
    """ File is for interacting with a singel file """

    NODE_TYPES = {ast.ClassDef: 'class',
                  ast.FunctionDef: 'def',
                  # ast.AsyncFunctionDef: 'async-def'
                  }

    def __init__(self, path: str):
        """ constructor """
        self._path = path
        self.nodes = {}
        for type_ in File.NODE_TYPES.values():
            self.nodes[type_] = {}

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
                        node.name = ast.unparse(node).split('\n')[0][6:-1]
                        node.__doc__ = ast.get_docstring(node)

                        new_body = []
                        for child in node.body:
                            # Class methods
                            if isinstance(child, ast.FunctionDef):
                                child.parent = node
                                new_body.append(child)
                            # Nested class support
                            if isinstance(child, ast.ClassDef):
                                child.parent = node
                                new_body.append(child)

                        node.body = new_body
                    # Functions
                    if isinstance(node, ast.FunctionDef):
                        node.__doc__ = ast.get_docstring(node)
                        node.name = ast.unparse(node).split('\n')[0][4:-1]

                        new_body = []
                        for child in node.body:
                            # Nested function support
                            if isinstance(child, ast.FunctionDef):
                                child.parent = node
                                new_body.append(child)

                        node.body = new_body

                    if isinstance(node, tuple(File.NODE_TYPES)):
                        # Only add root nodes with a name
                        if hasattr(node, 'name') and not hasattr(node, 'parent'):
                            type_ = File.NODE_TYPES.get(type(node))
                            self.nodes[type_][str(node.name)] = node

    def _recursive_tree(self, node, layer=0):
        type_ = File.NODE_TYPES.get(type(node))
        header = (type_ + " " + node.name).replace("*",
                                                   "\*").replace("__", "\_\_")
        docstring = '`'+str(node.__doc__)+'`'

        if type_ == 'class':
            header = '### ' + header
        elif type_ == 'def':
            header = "**" + header + "** \\"

        if layer > 0:
            print(">" * layer, header)
            print(">" * layer, docstring)
            print(">" * layer)
        else:
            print(header)
            print(docstring, end="\n\n")

        if len(node.body) > 0:
            for child in node.body:
                self._recursive_tree(child, layer+1)

    def output(self):
        """ outputs all node-types and their respective docstrings """

        # Use pipe for markdown files
        print("## %s" % (self._path))

        for type_ in self.nodes:
            for root_node in self.nodes[type_].values():
                self._recursive_tree(root_node)
        print('')
