salario_atual = float(input("Digite o salario atual do funcionario: "))
percentual_de_reajuste = float(input("Digite o percentual de ajuste: "))

valor_aumento = salario_atual * percentual_de_reajuste / 100
novo_salario = salario_atual + valor_aumento



print(f"O valor do aumento é: {valor_aumento:.2f}")
print(f"O novo salário é: {novo_salario:.2f}")
