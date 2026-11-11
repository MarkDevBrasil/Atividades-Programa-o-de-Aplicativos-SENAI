# 14. Jogo de adivinhação
# Defina um número secreto entre 1 e 50. O usuário terá até cinco tentativas para descobri-lo. Após
#cada erro, informe se o número secreto é maior ou menor que o palpite. Encerre quando houver
# acerto ou quando acabarem as tentativas.

import random

numero_secreto = random.randint(1, 50)
tentativas = 5

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}/{tentativas}: Digite um número entre 1 e 50: "))
    
    if palpite < 1 or palpite > 50:
        print("Número inválido. Tente novamente")
        continue
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior")
    else:
        print("O número secreto é menor")
else:
    print(f"Suas tentativas acabaram, o número secreto era: {numero_secreto}")