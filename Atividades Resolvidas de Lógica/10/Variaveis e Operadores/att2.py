# 2. Consumo de combustível
# Leia a distância percorrida por um veículo, em quilômetros, e a quantidade de combustível
#consumida, em litros. Calcule o consumo médio em km/L. Considere a quantidade de litros maior
# que zero.


distancia = float(input("Digite a distância percorrida em km: "))
combustivel = float(input("Digite a quantidade de combustivel consumido em litros: "))

consumo_m = distancia / combustivel

print(f"O consumo médio do veículo é de {consumo_m:.2f} km/L")