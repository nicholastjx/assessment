import unittest
from leastTransaction import testResult

class TestCases(unittest.TestCase):
    def test_1Person2PplWith2DP(self):
        person = {'Ali':40.105,'Bob':40.105,'Charlie':10.0}
        transaction = testResult(person)
        self.assertEqual(transaction, 2)
    
    def test_1Person2Ppl(self):
        person = {'Ali':40.105,'Bob':40.105,'Charlie':10.0}
        transaction = testResult(person)
        self.assertEqual(transaction, 2)
    
    def test_4ppl(self):
        person = {'Ali':10,'Bob':20,'Charlie':0,'Don':10}
        transaction = testResult(person)
        self.assertEqual(transaction, 1)
    
    def test_4ppl4With1PersonPayingSignificantlyMore(self):
        person = {'Ali':200,'Bob':80,'Charlie':50,'Don':20}
        transaction = testResult(person)
        self.assertEqual(transaction, 3)
    
    def test_4ppl4With2PersonPayingSignificantlyMore(self):
        person = {'Ali':160,'Bob':120,'Charlie':50,'Don':20, }
        transaction = testResult(person)
        self.assertEqual(transaction, 3)
        
if __name__ == '__main__':
    unittest.main()