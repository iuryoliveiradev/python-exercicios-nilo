## Exercício 3.4 - Converter metros para milímetros

# Solicitando o valor em metros
metro = int(input("Digite o valor em metros: "))

# Convertendo para milímetros
milimetro = metro * 1000

# Exibindo conversão
if metro == 1:
    print(f"1 metro é igual a {milimetro} milímetros")
else:
    print(f"{metro} metros são iguais a {milimetro} milímetros")