# 12. Soma dos múltiplos de três
# Leia um número inteiro positivo N. Calcule a soma de todos os números de 1 até N que sejam
# múltiplos de 3.

n = int(input("Digite um numero: "))

soma = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        soma += i

print(f"A soma dos múltiplos de 3 de 1 até {n} é: {soma}")