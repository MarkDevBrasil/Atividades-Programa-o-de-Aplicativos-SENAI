# Escreva um programa que peça ao usuário para inserir o raio de um círculo e exiba a área e a circunferência.

raio_c = float(input("Digite o raio do círculo: "))

area_c = 3.14159 * (raio_c ** 2)
circunferencia = 2 * 3.14159 * raio_c

print(f"A área do círculo é: {area_c:.2f}")
print(f"A circunferência do círculo é: {circunferencia:.2f}")