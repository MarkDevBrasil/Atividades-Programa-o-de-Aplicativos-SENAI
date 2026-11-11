# 16. Valores acima da média
# Leia seis preços e armazene-os em um vetor. Calcule a média dos preços e exiba quais valores
# ficaram acima dela.


preços = []

for i in range(6):
    preço = float(input(f"Digite o preço {i + 1}: "))
    preços.append(preço)
    

media = sum(preços) / len(preços)

print(f"A media dos preços é: {media:.2f}")

print("Valores acima da media:")
for preço in preços:
    if preço > media:
        print(f" - R$ {preço:.2f}")