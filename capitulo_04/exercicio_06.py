# Exercício 4.6 - Cálculo da mensalidade de um plano de celular da operadora Tchau

# Entrada do plano
plano = input("Qual é o seu plano de celular? ")

# Identificação do plano e definição de parâmetros
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50
elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99
else:
    print("Não conheço esse plano.")

# Entrada de minutos consumidos
minutos_consumidos = int(input("Quantos minutos você consumiu? "))

# Cálculo do suplemento
suplemento = 0
if minutos_consumidos > minutos_no_plano:
    suplemento = extra * (minutos_consumidos - minutos_no_plano)

# Saída dos valores
print("Você vai pagar:")
print(f"Preço do plano:     R${preco:.2f}")
print(f"Suplemento:         R${suplemento:.2f}")
print(f"Total:              R${preco + suplemento:.2f}")