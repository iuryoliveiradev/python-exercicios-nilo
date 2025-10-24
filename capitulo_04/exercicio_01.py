# Exercício 4.1 - Aplicação de multa caso o usuário ultrapasse 80 km/h

# Solicitando dados
velocidade = int(input("Você estava dirigindo em qual velocidade (km/h)? "))

# Verificação de velocidade permitida
if velocidade <= 80:
    print("Você estava dentro do limite de velocidade e não será multado!")
else:
    # Calculando valor da multa por excesso de velocidade
    excedente = velocidade - 80
    multa = excedente * 5

    # Exibindo valor da multa
    print(f"Você foi multado em R${multa:.2f}, pois ultrapassou {excedente} km/h do limite permitido!")