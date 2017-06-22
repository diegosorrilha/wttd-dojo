"""
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""


def saque(valor):
    # if valor in (40, 30):


    if valor == 40:
        notas = []
        max_nota = 20
        res = 40 // max_nota
        notas+=[max_nota] * res
        return notas

    if valor == 30:
        return [20, 10]

    if valor == 50:
        return [50]

    if valor == 10:
        return [10]