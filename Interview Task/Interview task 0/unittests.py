import unittest, os, convertor
from convertor.encode_convertor import encode
from pathlib import Path
from convertor.encode_convertor import encode as encod


KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'


class UnitTesting(unittest.TestCase):


    def test_0(self):
        texts="Privet HexTeam"
        code = encod(KEY_FILE)
        text=code.convert_text(texts)
        self.assertEqual(text, '|o|2!\\/\n37 #3><734|\\/|')
    
    def test_1(self):
        texts="Privet HexTeam"
        self.assertNotEqual(texts, '|o|2!\\/\n37 #3><734|\\/|')
    
    def test_2(self):
        texts="4|24<#|\|0"
        code = encod(KEY_FILE)
        text=code.convert_text(texts)
        self.assertEqual(text, 'arachno')        


if __name__ == '__main__':
    unittest.main()