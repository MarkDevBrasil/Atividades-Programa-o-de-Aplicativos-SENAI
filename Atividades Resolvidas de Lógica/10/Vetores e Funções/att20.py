# 20. Função de verificação de número primo
# Crie uma função que receba um número inteiro e retorne um valor lógico indicando se ele é
#primo. Utilize-a para verificar cinco números.
# Um número primo é maior que 1 e possui apenas dois divisores positivos: 1 e ele mesmo.

def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    primo = verifica_primo(num)
    numeros.append((num, primo))

for num, primo in numeros:
    if primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")

