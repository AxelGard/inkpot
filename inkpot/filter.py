def filter_file(file_path):
    """find the function and docstrings in the file"""
    flag = False
    last_func = ""

    doc_token = '"""'
    doc_open = None
    doc_close = None
    doc = ""

    table = {}
    with open(file_path, "r") as file:
        for cnt, line in enumerate(file):
            # print("Line {}: {}".format(cnt, line))
            if "def" in line:
                func = line.replace("def ", "")
                func = func.replace("\n", "")
                func = func.replace(":", "")
                table[func] = ""
                last_func = func
                flag = True
            elif flag:
                if not doc_open:
                    doc_open = (line.strip().find(doc_token), cnt)
                    # No docstring found
                    if doc_open[0] != 0:
                        table[func] = "no docstring"
                        doc_open = None
                        flag = False
                        continue

                if not doc_close:
                    doc_close = (line.strip().rfind(doc_token), cnt)
                    if doc_close == doc_open or doc_close[0] == -1:
                        doc_close = None

                doc += line.strip() + " "

                if doc_open and doc_close:
                    table[last_func] = doc.strip().strip(doc_token).strip().lower()
                    doc_open = None
                    doc_close = None
                    doc = ""
                    flag = False

    return table
