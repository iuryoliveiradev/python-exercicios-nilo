# Exercício 3.10 - Custo de aluguel de carro

# Solicitando informações para cálculo
km = float(input("Quantos km o carro percorreu? "))
dias = int(input("Por quantos dias o carro foi alugado? "))

# Definindo plural ou singular
quilometro = "quilômetro" if km == 1 else "quilômetros"
dia = "dia" if dias == 1 else "dias"

# Calculando valores a serem pagos
valor_km = km * 0.15  # R$0,15 por km rodado
valor_dia = dias * 60  # R$60,00 por dia
total = valor_km + valor_dia

# Mensagem de cobrança
print(
    f"O valor a ser pago pelo aluguel do carro é R${total:.2f}, "
    f"pois ele rodou um total de {km:.1f} {quilometro} (R${valor_km:.2f}) "
    f"por {dias} {dia} (R${valor_dia:.2f})"
)