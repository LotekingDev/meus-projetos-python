#!/usr/bin/env python3

# Inicia um loop que continuará até que o usuário decida sair
while True:
    # Exibe o menu de operações
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    # Recebe a escolha do usuário
    escolha = input("Digite o número da operação desejada: ")

    # Condicional para verificar se o usuário deseja sair
    if escolha == '5':
        print("Saindo do programa. Até logo!")
        break  # Sai do loop

    # Verifica se a escolha é válida (1 a 4)
    if escolha in ['1', '2', '3', '4']:
        # Solicita ao usuário que insira os números
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        # Realiza a operação correspondente à escolha do usuário
        if escolha == '1':
            resultado = num1 + num2
            print(f"A soma de {num1} e {num2} é {resultado}.")
        elif escolha == '2':
            resultado = num1 - num2
            print(f"A subtração de {num1} e {num2} é {resultado}.")
        elif escolha == '3':
            resultado = num1 * num2
            print(f"A multiplicação de {num1} e {num2} é {resultado}.")
        elif escolha == '4':
            # Verifica se o divisor é zero para evitar divisão por zero
            if num2 != 0:
                resultado = num1 / num2
                print(f"A divisão de {num1} por {num2} é {resultado}.")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        # Mensagem de erro para escolha inválida
        print("Escolha inválida. Tente novamente.")
