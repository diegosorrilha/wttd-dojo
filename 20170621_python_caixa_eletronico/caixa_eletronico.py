"""
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""


def saque(valor):
    # if valor in (40, 30):


    if valor == 40:
        notas = []
        max_nota = 20
        qtd, valor = divmod(valor, max_nota)
        notas+=[max_nota] * qtd
        return notas

    if valor == 30:
        notas = []
        max_nota = 20
        qtd, valor = divmod(valor, max_nota)
        notas += [max_nota] * qtd
        max_nota = 10
        qtd, valor = divmod(valor, max_nota)
        notas += [max_nota] * qtd
        return notas

    if valor == 50:
        return [50]

    if valor == 10:
        return [10]