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
        if  valor > 0:
             saldo += valor
             extrato += f"Depósito: R$ {valor:.2f}\n"
             print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
             print("Operação falhou! Valor informado é inválido.")
            
    elif opcao == "2":
        saque = float(input("Informe o valor que deseja sacar: "))
        if saque > saldo:
             print("Saque não realizado! Saldo insuficiente.")
        elif saque > limite:
             print("Saque não realizado! Limite da conta insuficiente.")
        elif numero_saques >= LIMITE_SAQUES:
             print("Saque não realizado! Limite de saques da conta excedido")
         
        elif saque > 0:
             saldo -= saque
             extrato += f"Saque: R$ {saque:.2f}\n"
             numero_saques += 1
             print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
         
        else:
             print("Saque não realizado! Valor informado é inválido.")




    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if not extrato:
             print("Não foram realizadas movimentações.")
        else:
             print(extrato)
             print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================\n")




    elif opcao == "4":
         print("Obrigado por usar nossos serviços, tenha um ótimo dia.")
         break

    else:
         print("Opção inválida, por favor selecione uma das opções:")



