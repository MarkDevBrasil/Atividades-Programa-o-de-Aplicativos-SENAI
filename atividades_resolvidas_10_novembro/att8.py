# Crie um programa que peça o valor de um produto e a porcentagem de desconto. Exiba o valor do desconto e o preço final do produto.


valor_p = float(input("Digite o valor do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

valor_desconto = valor_p * (desconto / 100)
preco_final = valor_p - valor_desconto

print(f"O valor do desconto é: R${valor_desconto:.2f}")
print(f"O preço final do produto é: R${preco_final:.2f}")