# Desenvolva um programa que troque o valor de duas variáveis. Por exemplo, se A=5 e B=10, ao final do programa A deve ser 10 e B deve ser 5.


a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

print(f"Antes - A: {a}, B: {b}")

a, b = b, a

print(f"Depois - A: {a}, B: {b}")