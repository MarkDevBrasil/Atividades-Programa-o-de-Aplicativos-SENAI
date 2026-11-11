# 10. Estacionamento
# Leia a quantidade inteira de horas que um veículo permaneceu estacionado, considerando pelo
# menos uma hora. A primeira hora custa R$ 8,00 e cada hora adicional custa R$ 3,00. O valor
# máximo cobrado por permanência é R$ 35,00. Calcule o valor a pagar.


horas = int(input("Digite a quantidade de horas que o veículo permaneceu estacionado: "))

if horas < 1:
    print("A quantiade não pode ser menos que 1 hora")
else:
    if horas == 1:
        valor = 8
    else:
        valor = 8 + (horas - 1) * 3
        
    if valor > 35:
        valor = 35
    print(f"O valor a pagar é R$ {valor:.2f}")