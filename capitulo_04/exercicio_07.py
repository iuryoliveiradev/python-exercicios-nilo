# Exercício 4.7 - Seletor de operação matemática entre dois valores fornecidos

# Solicitando dados para cálculo
num_01 = int(input("Qual o primeiro valor? "))
num_02 = int(input("E o segundo? "))

# Apresentando opções ao usuário
print("Menu de opções")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
opcao = int(input("Qual a opção desejada? "))

# Executando cálculo e apresentando resposta
if opcao == 1:
    resultado = num_01 + num_02
    print(f"{num_01} + {num_02} é igual a {resultado}")
elif opcao == 2:
    resultado = num_01 - num_02
    print(f"{num_01} - {num_02} é igual a {resultado}")
elif opcao == 3:
    resultado = num_01 * num_02
    print(f"{num_01} * {num_02} é igual a {resultado}")
elif opcao == 4:
    if num_02 == 0:
        print("Não é possível dividir por 0!")
        print("Tente novamente com outros valores.")
    else:
        resultado = num_01 / num_02
        print(f"{num_01} / {num_02} é igual a {resultado}")
else:
    print("Opção inválida.")