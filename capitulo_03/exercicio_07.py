# Exercício 3.7 - Desconto de mercadoria

# Solicitando informações
preco_produto = float(input("Qual o preço do produto? "))
desconto = float(input("Qual a porcentagem de desconto (%): "))

# Calculando desconto
valor_desconto = preco_produto * desconto / 100
novo_preco = preco_produto - valor_desconto

# Exibindo informações sobre o desconto
print(f"O produto custa R${preco_produto:.2f} e recebeu um desconto de R${valor_desconto:.2f} ({desconto}%) e passou a custar R${novo_preco:.2f}")