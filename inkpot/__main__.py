
"""
    FILE = "/home/axel/Programs/repositories/cira/cira/util.py"

    flag = False
    last_func = ""
    table = {}
    with open(FILE, 'r') as file:
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


    for func in table.keys():
        print(f"| %s |%s|" %(func, table[func]))

"""



if __name__ == "__main__":
    pass 