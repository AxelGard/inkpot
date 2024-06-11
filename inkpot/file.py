"""
class instance for one file
"""

import ast
from inkpot.astunparse import unparse 
from inkpot.config import MD_CHAR


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
            node_source = unparse(node).strip()
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
                docstring += MD_CHAR["doc_str_start"] + line + MD_CHAR["doc_str_end"] + " \\\n"
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
                print(MD_CHAR["depth"] * node.col_offset, header)
                print(MD_CHAR["depth"] * node.col_offset, docstring)
                print(MD_CHAR["depth"] * node.col_offset)
            else:
                print(header)
                print(docstring, end="\n\n")

        def visit_ClassDef(self, node):
            self.link_children(node)
            header =  MD_CHAR["class_def"] + " " + self.get_line_def(node)
            docstring = self.get_docstring(node)
            self.ouput(node, header, docstring)
            self.generic_visit(node)

        def visit_FunctionDef(self, node):
            self.link_children(node)
            header = MD_CHAR["function_def_start"] + self.get_line_def(node) + MD_CHAR["function_def_end"] + " \\"
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
                #print("Could not parse file:", self._path, self.parse_error)
                raise  ValueError("Could not parse file:", self._path, self.parse_error)
            else:
                print("%s %s" % (MD_CHAR["file_path"] ,self._path.replace("//", "/")))
                self.visitor = File.MarkDownVisitor()
                self.visitor.visit(self.tree)
            print("")
        else:
            #print("File must be parsed first. Use the \"parse()\" method")
            raise ValueError("File must be parsed first. Use the \"parse()\" method")


    def __str__(self):
        result = ""
        if self.tree is not None:
            if self.parse_error:
                raise  ValueError("Could not parse file:", self._path, self.parse_error)
            else:
                result += "%s %s" % (MD_CHAR["file_path"] ,self._path.replace("//", "/"))
                self.visitor = File.MarkDownVisitor()
                self.visitor.visit(self.tree)
            result += " "
        else:
            raise ValueError("File must be parsed first. Use the \"parse()\" method")
        return result