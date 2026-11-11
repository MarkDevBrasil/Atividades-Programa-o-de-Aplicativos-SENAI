#4. Divisão de uma conta
#Leia o valor total da conta de um restaurante e a quantidade de pessoas que irão dividi-la
#igualmente. Calcule quanto cada pessoa deverá pagar. Considere uma quantidade de pessoas
# maior que zero e exiba o valor com duas casas decimais.

valor_total = float(input("Digite o valor total da conta: "))
quantidade_p = int(input("Digite a quantidade de pessoas: "))

if quantidade_p > 0:
    valor_por_pessoa = valor_total / quantidade_p
    print(f"O valor que cada pessoa deverá pagar é: {valor_por_pessoa:.2f}")
else:
    print("Erro: A quantidade de pessoas deve ser maior que zero.")