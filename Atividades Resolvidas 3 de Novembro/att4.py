# Escreva um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa. O usuário deve informar o peso (em kg) e a altura (em metros).

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc:.2f}")
