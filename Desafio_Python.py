menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  '''

saldo = 0
limite = 500
extrato = ""
numero_saques=0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input ("Depósito:"))
        if deposito >0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("OPERAÇÃO NÃO REALIZADA. Valor Invalido")
    
    elif opcao == "s":
        saque = float(input("Saque:"))
        if saque<=500:
            if saldo >= saque:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= saque
                    numero_saques += 1
                    print(f"Número de saques realizados = {numero_saques}/3")
                    extrato += f"Saque: R$ {saque:.2f}\n"
                else:
                    print("OPERAÇÃO NÃO REALIZADA. Excedido o número de saques diários")
            else:
                print(f"OPERAÇÃO NÃO REALIZADA. Saldo Insuficiente, valor permitido para saque = R$ {saldo:.2f}")
        else:
            print("OPERAÇÃO NÃO REALIZADA. Valor máximo permitido para saque = R$500.00")    


    elif opcao == "e":
        print ("\n/////////////  EXTRATO  /////////////")
        print ("Não foram realizadas movimentações" if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}")
        print("///////////////////////////////////")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")