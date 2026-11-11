# 6. Verificação de múltiplos
# Leia dois números inteiros. Informe se o primeiro é múltiplo do segundo. Caso o segundo número
# seja zero, informe que a verificação não pode ser realizada.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero2 == 0:
    print("Erro")
else:
    if numero1 % numero2 == 0:
        print(f"{numero1} é multiplo de {numero2}")
    else:
        print(f"{numero1} não é multiplo de {numero2}")