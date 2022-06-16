import unittest

from translator import frenchToEnglish,englishToFrench


class TestFTE(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(None), None) 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 

        

class TestETF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(None), None) 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 

        
unittest.main()