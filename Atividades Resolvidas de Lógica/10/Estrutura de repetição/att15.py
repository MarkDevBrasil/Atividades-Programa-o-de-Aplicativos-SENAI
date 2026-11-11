# 15. Pesquisa de atendimento
#Leia avaliações de atendimento com valores de 1 a 5. O valor 0 encerra a pesquisa. Rejeite
#valores fora dessas opções. Ao final, apresente a quantidade de avaliações válidas e a média. Se
# nenhuma avaliação tiver sido registrada, informe essa situação.

availacoes = []

while True:
    avaliacao = int(input("Digite uma avaliação (1 a 5): "))
    if avaliacao == 0:
        break
    elif 1 <= avaliacao <= 5:
        availacoes.append(avaliacao)
    else:
        print("Valor invalidado, digite uma avaliação de 1 a 5: ")
        

if len(availacoes) > 0:
    media = sum(availacoes) / len(availacoes)
    print(f"Quantidade de avaliações válidas: {len(availacoes)}")
    print(f"Média das avaliações: {media:.2f}")
else:
    print("Nenhuma avaliação foi registrada.")
    
        