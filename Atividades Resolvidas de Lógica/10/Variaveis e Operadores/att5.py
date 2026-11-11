# 5. Troca de valores
#Leia dois valores e armazene-os nas variáveis A e B. Troque os conteúdos dessas variáveis
# utilizando uma variável auxiliar. Exiba os valores antes e depois da troca.

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

print(f"Antes da troca: A = {a}, B = {b}")

auxiliar = a
a = b
b = auxiliar

print(f"Depois da troca: A = {a}, B = {b}")