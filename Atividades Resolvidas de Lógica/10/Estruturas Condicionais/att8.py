#8. Cálculo de frete
#Leia o valor de uma compra e a região de entrega. Utilize as regras fictícias:
#• Local: R$ 15,00.
#• Estadual: R$ 30,00.
#• Nacional: R$ 50,00.
#Compras a partir de R$ 300,00 recebem frete grátis para qualquer uma das regiões válidas.
#Informe quando a região digitada for inválida. Apresente o frete e o total a pagar.


local = 15.00
estadual = 30.00
nacional = 50.00

valor_compra  = float(input("Digite o valor da compra: "))
regiao = input("Digite a região de entrega (Local, Estadual, Nacional): ").strip().lower()

if valor_compra >= 300:
    frete = 0.00
    print("Frete gratis")
elif regiao == "local":
    frete = local
    print(f"Frete: R$ {local:.2f}")
elif regiao == "estadual":
    frete = estadual
    print(f"Frete: R$ {estadual:.2f}")
elif regiao == "nacional":
    frete = nacional
    print(f"Frete: R$ {nacional:.2f}")
else:
    print("Região inválida")