# Crie uma rede bancaria precisa criar um novo menu de opções no sistema de atendimento aos clientes. O sistema deve permitir depositos, retiradas, consultar saldo. Crie um algoritimo que apresente essas opções . Desenvolva um menu com while true
saldo = 0
while True:
        print("============= BANCO MASTER ==============")
        print("1 - depositar")
        print("2 - sacar")
        print("3 - consultar saldo")
        print("4 - sair")
        print("5 - Falar com daniel vorcaro")
        escolha = input("Escolha uma opção:")
        if escolha == "1":
                valor = float(input("Digite o valor do deposito: "))
                saldo += valor
                print(f"Deposito realizado com sucesso, seu saldo atual é {saldo:.2f}")
        elif escolha == "2":
                valor = float(input("Digite o valor do saque: "))
                if valor <= saldo:
                    saldo -= valor
                print(f"saque feito com sucesso, seu saldo atual e {saldo:.2f}")
        elif escolha == "3":
            print(f"Seu saldo atual é: {saldo:.2f}")
        elif escolha == "4":
            break
        elif escolha == "5":
            print("Não roubei dinheiro de ninguem, sou trabalhador e honesto, #antipobres")
        else:
            print("Opção invalida, tente novamente")