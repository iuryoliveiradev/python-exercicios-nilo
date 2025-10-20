# Exercício 3.6 - Cálculo de aumento de salário

# Solicitando informações
salario = float(input("Qual o seu salário? "))
aumento = float(input("Qual a porcentagem de aumento (%): "))

# Calculando valores
valor_aumento = salario * aumento / 100
novo_salario = salario + valor_aumento

# Exibindo informações sobre o aumento
print(f"Seu salário de R${salario:.2f} recebeu um aumento de R${valor_aumento:.2f} ({aumento}%) e passou a ser R${novo_salario:.2f}")