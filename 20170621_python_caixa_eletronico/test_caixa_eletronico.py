import unittest
from caixa_eletronico import saque

"""
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

Exemplos:
Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
"""
class TestCaixaEletronico(unittest.TestCase):

    def test_saque_dez_reais(self):
        """Deve retornar uma nota de 10 reais"""
        notas = saque(10)
        self.assertListEqual([10], notas)

    def test_saque_trinta_reais(self):
        """Deve retornar uman nota de 20 e uma de 10 reais """
        notas = saque(30)
        self.assertListEqual([20, 10], notas)

    def test_saque_quarenta_reais(self):
        """Deve retornar duas notas de 20 reais"""
        notas = saque(40)
        self.assertListEqual([20, 20], notas)

    def test_saque_cinquenta_reais(self):
        """Deve retornar uma nota de 50 """

        notas = saque(50)
        self.assertListEqual([50], notas)

unittest.main()

