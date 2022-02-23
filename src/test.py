import unittest
from functions import *

class Df_test(unittest.TestCase):

    def test_get_paises(self):
        data=get_paises("https://restcountries.com/v2/all")
        self.assertIsNotNone(data)

    def test_get_df(self):
        data=get_paises("https://restcountries.com/v2/all")
        df=get_df(data)
        self.assertIsNotNone(df)

class export_test(unittest.TestCase):

    def test_export_to_sqlite(self):
        data=get_paises("https://restcountries.com/v2/all")
        df=get_df(data)
        self.assertEqual(export_to_sqlite(df),True)

    def test_export_to_json(self):
        data=get_paises("https://restcountries.com/v2/all")
        df=get_df(data)
        self.assertEqual(export_to_json(df),True)

if __name__ == "__main__":
    unittest.main()