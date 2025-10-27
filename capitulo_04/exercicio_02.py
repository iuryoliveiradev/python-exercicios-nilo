# Exercício 4.2 - Identifica o maior e o menor entre três números fornecidos pelo usuário

# Solicitando informações
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

# Inicializando maior e menor com o primeiro valor
maior = a
menor = a

# Verificando maior
if b > maior:
    maior = b
if c > maior:
    maior = c

# Verificando menor
if b < menor:
    menor = b
if c < menor:
    menor = c

# Exibindo resultado
print(f"O maior número informado foi {maior}.")
print(f"O menor número informado foi {menor}.")
