# Desenvolva um programa que peça ao usuário para digitar três notas e, em seguida, exiba a média aritmética delas com uma mensagem clara.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"A media das notas foram: {media:.2f}")