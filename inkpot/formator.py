
def table_format(file_info:dict):
    """ Takes a dict  """
    print("| def | doc-str |")
    print("| --- | --- |")
    for func in file_info.keys():
        print(f"| %s | %s |" %(func, file_info[func]))
    print("")

def file_header(name):
    """ outputs the neme header """
    print("## %s" %(name))


def main_header(name):
    print("# %s" %(name))
