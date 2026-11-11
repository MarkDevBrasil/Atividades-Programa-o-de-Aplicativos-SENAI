# 18. Comparação entre vetores
#Leia dois vetores, A e B, com cinco números inteiros cada. Crie um terceiro vetor, C, no qual cada
#posição contenha a soma dos valores das posições correspondentes de A e B. Exiba o vetor
# resultante.


vetor_a = []
vetor_b = []
vetor_c = []

for i in range(5):
    numero_a = int(input(f"Digite o {i + 1}º número do vetor a: "))
    vetor_a.append(numero_a)

for i in range(5):
    numero_b = int(input(f"Digite o {i + 1}º número do vetor a: "))
    vetor_b.append(numero_b)

for i in range(5):
    soma = vetor_a[i] + vetor_b[i]
    vetor_c.append(soma)

print("Vetor c (soma dos elementos correspondentes):", vetor_c)

