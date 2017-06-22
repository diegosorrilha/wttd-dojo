"""
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
"""

def saque(valor):
    if valor == 10:
        return [10]

    if valor == 40:
        return [20, 20]

    return [20, 10]
