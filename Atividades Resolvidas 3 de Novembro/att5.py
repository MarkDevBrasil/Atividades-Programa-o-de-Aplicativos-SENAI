# Crie um programa que receba o valor da conta de um restaurante e calcule a gorjeta do garçom (10% do valor da conta).


valor_conta = float(input("Digite o valor da conta do restaurante: "))

gorjeta = valor_conta * 0.10

print(f"A gorjeta do garçom é: R${gorjeta:.2f}")
