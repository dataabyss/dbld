# test/my_mod_test.py

import unittest

from my_lambdata.assignment import CustomFrame

class TestCustomFrame(unittest.TestCase):

    def test_add_state_names(self):

        custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})

        breakpoint()

        custom_df.add_state_names()
        #self.assertEqual(True, True)
        
if __name__ == '__main__':
    unittest.main()