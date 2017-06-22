"""
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""


def maior_nota_possivel(valor):
    for nota in (100, 50, 20, 10):
        if valor // nota > 0:
            return nota


def saque(valor):
    notas = []
    while valor > 0:
        max_nota = maior_nota_possivel(valor)
        qtd, valor = divmod(valor, max_nota)
        notas += [max_nota] * qtd
    return notas
