#===========================task3(worksheet2.1)===========================

import unittest
import morse
import ham

class TestMorse(unittest.TestCase):
    
    def test(self):
        self.assertTrue(True)
    
    def test_encode_us(self):
        self.assertEqual(morse.encode("US"), '..- ...')
        self.assertEqual(morse.encode("pe"), '..- ...')
        self.assertEqual(morse.encode('te'), '..- ...')
        self.assertEqual(morse.encode('re'), '..- ...')
        self.assertEqual(morse.encode('Mo'), '..- ...')

    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'),'US')
        self.assertEqual(morse.decode('.--. .'),'PE')
        self.assertEqual(morse.decode('- .'),'TE')
        self.assertEqual(morse.decode('.-. .'),'RE')
        self.assertEqual(morse.decode('-- ---'),'MO')

    def test_Tree(self):
        self.assertEqual(morse.Node.value,1)
    def test_Empty_Tree(self):
        self.assertEqual(morse.Node.value,None)
    def test_insert(self):
        tree= morse.Node()
        tree.dot.dash.dash.dash.dash  = morse.Node("1")
    def test_find(self):
        morse.Conv_letter_to_Morse(morse.Node(), 'A','dot.dash')

    def insertSymbol(self):
        tree=morse.Node()
        self.assertTrue(tree.dot.dash.dot.dash.dot.dash,".")
    def encode_ham_test(self):
        self.assertEqual(ham.encode_ham('s1', 'r1', 'hi'),'.-. .---- -.. . ... .---- -...- .... .. -...- -.--.')
    
    def decode_ham_test(self):
        self.assertEqual(ham.decode_ham('.-. .---- -.. . ... .---- -...- .... .. -...- -.--.'),'r1des1=hi=(')

if __name__ == '__main__':
    unittest.main()
