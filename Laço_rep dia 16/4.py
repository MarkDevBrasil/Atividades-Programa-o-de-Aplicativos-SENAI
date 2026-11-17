# Escreva um programa que leia dois numeros. Imprima a divisão inteira do primeiro pelo segundo, assim com o resto da divisão, utilize apenas os operadores de soma e subtração para calcular o resultado. lembre-se de que podemos enter o quiociente da divisão de dois numeros como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20/4=4, uma vez que podemos subtrair


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
    
dividendo = numero1
divisor = numero2
quociente = 0

if divisor == 0:
    print("Não é possivel dividir por zero")
else:
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
print("=================================")
print(f"dividendo: {numero1}")
print(f"divisor: {numero2}")
print(f"quociente: {quociente}")
print(f"resto: {dividendo}")