#11. Contagem regressiva
#Leia um número inteiro positivo e exiba uma contagem regressiva desse número até zero. Ao
# final, apresente a mensagem: “Contagem encerrada!”.

numero = int(input("Digite um número inteiro positivo: "))

if numero < 0:
    print("Invalido o numero tem que ser maior q zero")
else:
    for i in range(numero, -1, -1):
        print(i)
    print("Contagem encerrada!")