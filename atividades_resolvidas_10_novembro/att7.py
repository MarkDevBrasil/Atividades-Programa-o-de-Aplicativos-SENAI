# Desenvolva um programa que leia a altura e o peso de uma pessoa e calcule seu IMC, exibindo o resultado com duas casas decimais.

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

imc = peso / (altura ** 2)

print(f"Seu imc é: {imc:.2f}")
