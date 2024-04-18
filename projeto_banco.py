menu = """

[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques=0
LIMITE_SAQUES=3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor=float(input("Informe o valor do deposito:"))

        if valor > 0 :
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

        else:
            print("Operaçao falhou o valor informado é invalido")

    elif opcao == "2":
        valor=float(input("informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operaçao falha Saldo insuficiente")

        elif excedeu_limite:
            print("Operaçao falha Valor do Saque excedeu o limite")

        elif excedeu_saques:
            print("Operaçao invalida Numero de saques diario excedidos ")
        
        elif  valor > 0 :
            saldo -= valor
            extrato +=f"Saque:R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operaçao invalida Valor inserido invalido")


    elif opcao =="3":
        print("\n__________EXTRATO__________")
        print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo:R$ {saldo:.2f}\n")
        print("_____________________________")

    elif opcao == "0":
        break

    else:
        ("operaçao invalida , por favor selecione novamente a operaçao desejada")