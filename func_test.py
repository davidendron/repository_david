import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal # <-- for testing dataframes

# Functions


# Test Functions

class DFTests(unittest.TestCase):

    """Class for running tests
    IN"""

    def setUp(self):
        """ Load data from csv, the data must be in the same directory"""
        try:

            tableS6= pd.read_excel("schmidt_data.xlsx",sheet_name="Table S6",skiprows=2)
            #tableS23= pd.read_excel("schmidt_data.xlsx",sheet_name="Table S23",skiprows=2) # Table with the growth rate data

        except IOError:
            print('cannot open file')
        self.fixture = tableS6

    def test_dataFrame_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect
        In this case, both dataframes should be different, a failed
        test will confirm this"""
        foo = tableS23= pd.read_excel("schmidt_data.xlsx",sheet_name="Table S23",skiprows=2)
        assert_frame_equal(self.fixture, foo)

        
if __name__ == '__main__':
    unittest.main()