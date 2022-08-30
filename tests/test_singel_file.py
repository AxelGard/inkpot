import inkpot

class TestSingleFile:
    """test a single file with inkpot."""
    
    def test_add_file(self):
        """ test the add file """
        wanted_output = "# .ex/add.py ## .ex/add.py  "
        path = ".ex/add.py"
        file = inkpot.directory.Directory(path)
        file.parse_files()
        output = str(file)
        output = output.replace("\n", "")
        assert output == wanted_output 