import unittest
from caixa_eletronico import caixa_eletronico

class TestCaixaEletronico(unittest.TestCase):

    def test_caixa_eletronico(self):
        self.assertEqual(caixa_eletronico(), None)

unittest.main()
        
