import inkpot

class TestSingleFile: 
    def test_add_file(self):
        expected_output = """
            # tests/.ex/add.py
            ## tests/.ex/add.py
            **def add(a, b)** \
            `add to objects `
        """
        
        