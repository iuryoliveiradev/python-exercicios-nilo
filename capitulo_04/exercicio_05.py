# Exercício 4.5 - Calcula o preço da passagem de acordo com a distância

# Entrada de dados
distancia = int(input("Qual a distância que deseja percorrer em km? "))

# Definindo valor por km conforme distância
if distancia <= 200:
    valor = 0.50
else:
    valor = 0.45

# Calculando valor total da passagem
valor_passagem = distancia * valor

# Exibindo valor final da passagem ao passageiro
print(f"O valor da sua passagem é de R${valor_passagem:.2f}")