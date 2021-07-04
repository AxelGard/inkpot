"""
class instance for one file
"""


class File:
    """ File is for interacting with a singel file """

    def __init__(self, path:str):
        """ constructor """
        self._path = path
        self.table = {}

    def filter(self):
        """ find the function and docstrings in the file """
        flag = False
        last_func = ""

        doc_token = '"""'
        doc_open = None
        doc_close = None
        doc = ""

        self.table = {}
        with open(self._path, "r") as file:
            for cnt, line in enumerate(file):
                if line.lstrip().find("def ") == 0:
                    func = line.replace("def ", "")
                    func = func.replace("\n", "")
                    func = func.replace(":", "")
                    self.table[func] = ""
                    last_func = func
                    flag = True
                elif flag:
                    if not doc_open:
                        doc_open = (line.strip().find(doc_token), cnt)
                        # No docstring found
                        if doc_open[0] != 0:
                            self.table[func] = "no docstring"
                            doc_open = None
                            flag = False
                            continue

                    if not doc_close:
                        doc_close = (line.strip().rfind(doc_token), cnt)
                        if doc_close == doc_open or doc_close[0] == -1:
                            doc_close = None

                    doc += line.strip() + " "

                    if doc_open and doc_close:
                        self.table[last_func] = doc.strip().strip(doc_token).strip()
                        doc_open = None
                        doc_close = None
                        doc = ""
                        flag = False
        return self.table


    def output(self):
        """ outputs all def and its doc str  """
        print("# %s" %(self._path))
        print("| def | doc-str |")
        print("| --- | --- |")
        for func, docstr in self.table.items():
            print("| %s | %s |" %(func, docstr))
        print("")
