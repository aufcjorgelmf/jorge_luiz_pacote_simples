# meu_pacote/entrada.py

from .operacoes import somar_numeros

def solicitar_numeros():
    try:
        qtd = int(input("Quantos números você deseja somar? "))
        numeros = []

        for i in range(qtd):
            num = float(input(f"Digite o {i+1}º número: "))
            numeros.append(num)

        resultado = somar_numeros(numeros)
        print(f"A soma dos números é: {resultado}")
        return resultado

    except ValueError:
        print("Por favor, insira apenas números válidos.")
