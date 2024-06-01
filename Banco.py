menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0

running = True

def inputValor () :
    valor = -1
    while (valor == -1) :
        valorInput = input ("Valor:")
        try :
            int (valorInput)
        except :
            print ("Insira um número")
        else :
            if (int(valorInput) < 0) :
                print ("Digite um número positivo")
            else :
                valor = valorInput
                return int(valor)

while running:
    opcao = input(menu)

    if opcao == "d":
        print ("Depósito")
        valor = inputValor ()
        extrato += f"\n+[R${valor}]"
        saldo += valor

    elif opcao == "s":
        print ("Saque")
        if numeroSaques < 3 :
            valor = inputValor ()
            if (valor <= saldo) :
                if (valor <= 500) :
                    extrato += f"\n-[R${valor}]"
                    saldo -= valor
                    numeroSaques += 1
                else :
                    print ("Limite de saque excedido")
            else :
                print ("Saldo insuficiente")
        else :
            print ("Limite de saques atingido")

    elif opcao == "e":
        print ("================ Extrato ================")
        print (f"Saque: R$ {saldo}\n")
        print (extrato)
        print ("\n=========================================")


    elif opcao == "q":
        running = False

    else:
        print ("Operação inválida!")