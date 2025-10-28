# Exercício 4.3 - Calcula aumento salarial conforme faixa de salário

# Entrada de dados
salario = float(input("Qual o seu salário? "))

# Determinando a porcentagem de aumento com base no salário
if salario > 1250.00:
    porcentagem = "(10%)"
    aumento = salario * 0.10
else:
    porcentagem = "(15%)"
    aumento = salario * 0.15

# Cálculo do novo salário
novo_salario = salario + aumento

# Saída de resultados
print(f"Seu salário de R${salario:.2f} teve aumento de R${aumento:.2f} {porcentagem} e passou a ser de R${novo_salario:.2f}")