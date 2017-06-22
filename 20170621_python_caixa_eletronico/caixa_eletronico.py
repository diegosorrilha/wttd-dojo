"""
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""


def saque(valor):
    if valor in (40, 30, 10):
        notas = []
        max_nota = 20
        while valor > 0:
            qtd, valor = divmod(valor, max_nota)
            notas += [max_nota] * qtd
            max_nota = 10
        return notas


    if valor == 50:
        return [50]

