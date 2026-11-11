# 9. Aprovação por nota e frequência
#Leia a média final e o percentual de frequência de um aluno. Ele será aprovado se tiver média
#maior ou igual a 7 e frequência maior ou igual a 75%. Caso contrário, informe se a reprovação
#ocorreu por nota, frequência ou pelos dois motivos.

media_f = float(input("Digite a média final do aluno: "))
frequencia = float(input("Digite o percentual de frequencia: "))

if media_f >= 7 and frequencia >= 75:
    print("Aluno aprovado")
else:
    if media_f < 7 and frequencia < 75:
        print("Aluno reprovado por nota e frequencia: ")
    elif media_f < 7:
        print("Aluno reprovado por nota")
    else:
        print("Aluno reprovado por frequencia")