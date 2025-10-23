# Exercício 3.11 - Tempo de vida perdido por cigarro fumado

# Coletando informações
cigarros_por_dia = int(input("Qual a média de cigarros você fuma por dia? "))
anos_fumando = int(input("E por quantos anos você já fuma? "))

# Calculando dias de vida perdidos por fumar
minutos_perdidos = cigarros_por_dia * 10 * anos_fumando * 365
dias_perdidos = int(minutos_perdidos / 1440)

# Plural da mensagem
dia = "dia" if dias_perdidos == 1 else "dias"

# Exibindo mensagem
print(f"Você já diminuiu sua vida em {dias_perdidos} {dia}!")