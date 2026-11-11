# Desenvolva um programa que calcule o consumo médio de um automóvel. O usuário deve informar a distância percorrida e o total de combustível gasto.


consumo_medio = float(input("Digite a distância percorrida (em km): "))
combustivel = float(input("Digite o total de combustível gasto (em litros): "))

if combustivel == 0:
    print("O valor do combustivel não pode ser zero")
else:
    consumo_m = consumo_medio / combustivel
    print(f"O consumo médio : {consumo_m:.2f} km/l")