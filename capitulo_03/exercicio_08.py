# Exercício 3.8 - Cálculo de tempo gasto em viagem

# Solicitando informações
distancia = int(input("Qual a distância a ser percorrida em KM? "))
velocidade_media = int(input("Qual a velocidade média estipulada durante a viagem? "))

# Calculando tempo gasto (em horas)
tempo = distancia / velocidade_media

# Mensagem exibindo o tempo
print(f"A duração prevista, caso mantenha a velocidade de {velocidade_media} KM/h, é de {tempo:.2f} hora(s).")