# Exercício 4.5 - Calcula o preço da passagem de acordo com a distância

# Coletando informações para calculo
distancia = int(input("Qual a distância que deseja percorer em km? "))

# Definindo preço por km total
if distancia <= 200:
    valor = 0.50
else:
    valor = 0.45

# Descobrindo valor da passagem para cobrança
valor_passagem = distancia * valor

# Exibindo informação ao passageiro
print(f"O valor da sua passagem é de R${valor_passagem:.2f}")