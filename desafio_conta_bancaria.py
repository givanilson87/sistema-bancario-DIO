menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou: Valor Inválido")

    elif opcao == "2":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saque = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")

        elif execedeu_limite:
            print("O valor do saldo excede o limite")

        elif execedeu_saque:
            print("Saques excedidos!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("O valor informado é Invalido")

    elif opcao == "3":
        print("\n ------ EXTRATO -----")
        print("Nãou houve movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------------")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida!!")
