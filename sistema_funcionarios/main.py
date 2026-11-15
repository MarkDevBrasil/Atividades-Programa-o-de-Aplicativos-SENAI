from db import conectar


nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
percentual = float(input("Digite o percentual de aumento: "))


valor_aumento = salario * (percentual / 100)

salario_final = salario + valor_aumento


print("====== RESULTADO ========")
print(f"Nome do funcionário: {nome}")
print(f"Salário atual: R$ {salario:.2f}")
print(f"Percentual de aumento: {percentual:.2f}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {salario_final:.2f}")

conexao = conectar()

cursor = conexao.cursor()

sql = "insert into funcionarios (nome, salario_atual, percentual_aumento, valor_aumento, salario_final) values (%s, %s, %s, %s, %s)"

valores = (
    nome,
    salario,
    percentual,
    valor_aumento,
    salario_final
)


cursor.execute(sql, valores)

conexao.commit()

print("Funcionário cadastrado com sucesso!")

cursor.close()
conexao.close()

    