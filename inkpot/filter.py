
def filter_file(file_path):
    """ find the function and docstrings in the file """
    flag = False
    last_func = ""
    table = {}
    with open(file_path, 'r') as file:
        for cnt, line in enumerate(file):
            #print("Line {}: {}".format(cnt, line))
            if "def" in line:
                func = line.replace("def ", '')
                func = func.replace('\n', '')
                func = func.replace(':', '')
                table[func] = ""
                last_func = func
                flag = True
            elif flag:
                doc = line.replace('\n', '')
                doc = doc.replace('  ', '')
                doc = doc.replace('"""', '')
                table[last_func] = doc
                flag = False
    return table
