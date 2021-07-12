"""
class instance for one file
"""

import ast
import astunparse


class File:
    """ File is for interacting with a single file """

    class MarkDownVisitor(ast.NodeVisitor):
        """
        A custom NodeVisitor class for markdown files. 
        When a class or function are visited their
        names and docstrings are printed.
        """

        @staticmethod
        def get_line_def(node):
            node_source = astunparse.unparse(node).strip()
            node_source_split = node_source.split("\n")
            for i, line in enumerate(node_source_split):
                if line.strip()[-1] == ":":
                    node_source = " \\\n".join(node_source_split[:i+1])[:-1]
                    break
            return node_source.replace("*", "\\*").replace("__", "\\_\\_")

        @staticmethod
        def get_docstring(node):
            docstring = ""
            for line in str(ast.get_docstring(node)).split("\n"):
                docstring += "`" + line + "` \\\n"
            docstring = docstring.rstrip().rstrip("\\")
            return docstring

        @staticmethod
        def link_children(node):
            # Root node
            if not hasattr(node, "parent"):
                node.col_offset = 0

            for child in node.body:
                child.parent = node
                # Override "col_offset" with cutsom indentation
                child.col_offset = node.col_offset + 1

        @staticmethod
        def ouput(node, header, docstring):
            if node.col_offset > 0:
                print(">" * node.col_offset, header)
                print(">" * node.col_offset, docstring)
                print(">" * node.col_offset)
            else:
                print(header)
                print(docstring, end="\n\n")

        def visit_ClassDef(self, node):
            self.link_children(node)
            header = "### " + self.get_line_def(node)
            docstring = self.get_docstring(node)
            self.ouput(node, header, docstring)
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            self.link_children(node)
            header = "**" + self.get_line_def(node) + "** \\"
            docstring = self.get_docstring(node)
            self.ouput(node, header, docstring)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):
            self.visit_FunctionDef(node)

    def __init__(self, path: str):
        """ constructor """
        self._path = path
        self.source = ""
        self.parse_error = None
        self.tree = None
        self.visitor = None

    def parse(self):
        """ parse the file """
        with open(self._path, "rb") as src:
            if hasattr(src, "read"):
                self.source = src.read()
                try:
                    self.tree = ast.parse(self.source)
                except SyntaxError as e:
                    self.parse_error = e

    def output(self):
        """ outputs all node-types and their respective docstrings """
        if self.tree is not None:
            if self.parse_error:
                print("Could not parse file:", self._path, self.parse_error)
            else:
                print("## %s" % (self._path.replace("//", "/")))
                self.visitor = File.MarkDownVisitor()
                self.visitor.visit(self.tree)
            print("")
        else:
            print("File must be parsed first. Use the \"parse()\" method")
