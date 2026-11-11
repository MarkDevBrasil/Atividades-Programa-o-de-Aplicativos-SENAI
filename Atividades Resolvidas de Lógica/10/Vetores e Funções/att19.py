# 19. Função de conversão de distância
#Crie uma função que receba uma distância em quilômetros e retorne o valor em metros. Utilize a
# função para converter três distâncias informadas pelo usuário.

def converter_distancia(km):
    return km * 1000


distancias = []

for i in range(3):
    km = float(input(f"Digite a {i+1}ª distância em quilômetros: "))
    metros = converter_distancia(km)
    distancias.append(metros)
    
print("As distâncias convertidas em metros são:", distancias)