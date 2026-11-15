# Faça um programa que leia o lado de um quadrado e exiba sua área e seu perímetro

lado = float(input("Digite o lado do quadrado: "))

area = lado ** 2
perimetro = 4 * lado

print(f"A área do quadrado é: {area:.2f}")
print(f"O perímetro do quadrado é: {perimetro:.2f}")