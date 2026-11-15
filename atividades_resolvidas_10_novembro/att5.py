# Crie um programa que leia dois números e mostre a soma, a subtração, a multiplicação e a divisão, com mensagens que identifiquem cada operação.


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
if num2 != 0:
    divisao = num1 / num2

print(f"A soma dos números é: {soma}")
print(f"A subtração dos números é: {subtracao}")
print(f"A multiplicação dos números é: {multiplicacao}")
if num2 != 0:
    print(f"A divisão dos números é: {divisao}")