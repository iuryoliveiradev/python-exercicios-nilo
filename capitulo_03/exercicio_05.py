# Exercício 3.5 - Converter dias, horas, minutos e segundos informados pelo usuário em segundos

# Solicitando informações
dia = int(input("Digite um valor em dias: "))
hora = int(input("Agora um valor em horas: "))
minuto = int(input("Um valor em minutos: "))
segundo = int(input("Por último, os segundos: "))

# Soma tudo e converte para segundos
total_segundos = dia * 86400 + hora * 3600 + minuto * 60 + segundo

# Exibe o resultado final
print(f"{dia} dia(s), {hora} hora(s), {minuto} minuto(s) e {segundo} segundo(s) são {total_segundos} segundo(s)")