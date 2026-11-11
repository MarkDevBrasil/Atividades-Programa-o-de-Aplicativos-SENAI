# 17. Contagem de ocorrências
# Leia dez números inteiros e armazene-os em um vetor. Depois, solicite um número para pesquisa
# e informe quantas vezes ele aparece no vetor.

numeros = []


for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
    
pesquisa = int(input("Digite um numero para pesquisa: "))

contagem = numeros.count(pesquisa)
print(f"O número {pesquisa} aparece {contagem} vezes no vetor.")

