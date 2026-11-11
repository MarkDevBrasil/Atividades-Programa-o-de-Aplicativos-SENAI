# Crie um programa que leia o valor de um depósito e o valor da taxa de juros. Calcule e imprima o valor do rendimento e o valor total depois do rendimento.


deposito = float(input("Digite o valor do depósito: "))
valor_taxa = float(input("Digite o valor da taxa de juros (em %): "))

valor_rendimento = deposito * valor_taxa / 100
valor_total = deposito + valor_rendimento

print(f"O valor do rendimento é: {valor_rendimento:.2f}")
print(f"O valor total depois do rendimento é: {valor_total:.2f}")
