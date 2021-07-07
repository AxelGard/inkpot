"""
class instance for one file
"""

import ast
import astunparse

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
        self.parse_error = None

    def filter(self):
        """ find node-types and docstrings in the file """
        with open(self._path, 'rb') as source:
            if hasattr(source, 'read'):
                source = source.read()
                try:
                    tree = ast.parse(source)
                except SyntaxError as e:
                    self.parse_error = e
                else:
                    for node in ast.walk(tree):
                        # Classes
                        if isinstance(node, ast.ClassDef):
                            node.__doc__ = ast.get_docstring(node)
                            node.name = astunparse.unparse(ast.parse(node)).split('\n')[2][6:-1]

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

                            node.name = astunparse.unparse(ast.parse(node)).split('\n')[2][4:-1]

                            new_body = []
                            for child in node.body:
                                # Nested function support
                                if isinstance(child, ast.FunctionDef):
                                    child.parent = node
                                    new_body.append(child)

                            node.body = new_body

                        if isinstance(node, tuple(File.NODE_TYPES)):
                            # Only add root nodes, they must also have a name
                            if hasattr(node, 'name') and not hasattr(node, 'parent'):
                                type_ = File.NODE_TYPES.get(type(node))
                                self.nodes[type_][str(node.name)] = node

    @staticmethod
    def recursive_tree(node, layer=0):
        type_ = File.NODE_TYPES.get(type(node))
        header = (type_ + " " + node.name).replace("*",
                                                   "\*").replace("__", "\_\_")
        docstring = ""
        for line in str(node.__doc__).split('\n'):
            docstring += '`' + line + '` \\\n'
        docstring = docstring.rstrip().rstrip('\\')

        if type(node) == ast.ClassDef:
            header = '### ' + header
        elif type(node) == ast.FunctionDef:
            header = '**' + header + '** \\'

        if layer > 0:
            print(">" * layer, header)
            print(">" * layer, docstring)
            print(">" * layer)
        else:
            print(header)
            print(docstring, end="\n\n")

        if len(node.body) > 0:
            for child in node.body:
                File.recursive_tree(child, layer+1)

    def output(self):
        """ outputs all node-types and their respective docstrings """

        print('## %s' % (self._path))
        if self.parse_error:
            print("Could not parse file:", self._path, self.parse_error)
        for type_ in self.nodes:
            for root_node in self.nodes[type_].values():
                File.recursive_tree(root_node)
        print('')
