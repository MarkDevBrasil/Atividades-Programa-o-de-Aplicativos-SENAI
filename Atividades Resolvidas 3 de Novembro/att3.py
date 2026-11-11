# Faça um programa que leia o nome de um produto, seu preço e a quantidade comprada. Exiba o valor total a ser pago.


produto = input("Digite o nome do produto: ")
preço = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

valor_total = preço * quantidade

print(f"O valor total a ser pago pelo produto {produto} é: R${valor_total:.2f}")
