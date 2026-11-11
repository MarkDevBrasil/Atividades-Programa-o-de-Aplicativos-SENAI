# 13. Fatorial
# Leia um número inteiro de 0 a 10 e calcule seu fatorial utilizando uma estrutura de repetição.
# Solicite novamente caso o valor esteja fora do intervalo.
# Exemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120. Considere 0! = 1.

while True:
    numero = int(input("Digite um numero inteiro de 0 a 10: "))
    if 0 <= numero <= 10:
        break
    print("Valor inválido. Digite um número de 0 a 10.")

fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é: {fatorial}")