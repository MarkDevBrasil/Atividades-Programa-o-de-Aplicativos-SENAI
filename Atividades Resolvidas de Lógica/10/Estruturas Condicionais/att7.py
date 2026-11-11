# 7. Classificação de triângulos
# Leia três medidas positivas. Primeiro, verifique se elas podem formar um triângulo: cada medida
#deve ser menor que a soma das outras duas. Se formarem, classifique-o:
#• Equilátero: três lados iguais.
#• Isósceles: exatamente dois lados iguais.#
#• Escaleno: três lados diferentes.

lado1 = float(input("Digite um lado: "))
lado2 = float(input("Digite outro lado: "))
lado3 = float(input("Digite o último lado: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("As medias devem ser positivas")
elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Triangulo equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")