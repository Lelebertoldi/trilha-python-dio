# Variáveis globais
usuarios = []
contas = []
numero_conta = 0o00001

# Funções
def criar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    # Remover pontos e traços do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verificar se já existe um usuário com este CPF
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Usuário já existe!")
        return
    
    # Criar novo usuário e adicionar à lista
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")

def criar_conta_corrente(cpf):
    global numero_conta, contas
    # Filtrar usuário pelo CPF
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    if not usuario:
        print("Usuário não encontrado!")
        return
    
    # Criar nova conta corrente e adicionar à lista
    conta = {
        'agencia': '0001',
        'numero_conta': numero_conta,
        'usuario': usuario
    }
    contas.append(conta)
    numero_conta += 1
    print("Conta corrente criada com sucesso!")

def verificar_dados(cpf):
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)
    
    if not usuario:
        print("Usuário não encontrado!")
        return
    
    print(f"Nome: {usuario['nome']}")
    print(f"Data de Nascimento: {usuario['data_nascimento']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Endereço: {usuario['endereco']}")
    print("Contas Correntes:")
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            print(f"Agência: {conta['agencia']} | Número da Conta: {conta['numero_conta']}")

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Operação falhou! Valor informado é inválido.")
    return saldo, extrato

def saque(*, valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if valor > saldo:
        print("Saque não realizado! Saldo insuficiente.")
    elif valor > limite:
        print("Saque não realizado! Limite da conta insuficiente.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Saque não realizado! Limite de saques da conta excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Saque não realizado! Valor informado é inválido.")
    return saldo, extrato, numero_saques

def extrato(*, saldo, extrato):
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
    print("=============================\n")

# Main Loop
saldo = 0
limite = 500
extrato_str = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuario_logado = None

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Verificar Dados
[7] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "1":
        if not usuario_logado or not any(conta['usuario'] == usuario_logado for conta in contas):
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato_str = deposito(valor, saldo, extrato_str)

    elif opcao == "2":
        if not usuario_logado or not any(conta['usuario'] == usuario_logado for conta in contas):
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        valor = float(input("Informe o valor que deseja sacar: "))
        saldo, extrato_str, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato_str, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

    elif opcao == "3":
        if not usuario_logado or not any(conta['usuario'] == usuario_logado for conta in contas):
            print("Operação não permitida! Crie um usuário e uma conta corrente primeiro.")
            continue
        extrato(saldo=saldo, extrato=extrato_str)

    elif opcao == "4":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
        usuario_logado = next((usuario for usuario in usuarios if usuario['cpf'] == cpf.replace(".", "").replace("-", "")), None)

    elif opcao == "5":
        cpf = input("Informe o CPF do usuário para criar uma conta corrente: ")
        criar_conta_corrente(cpf)
        usuario_logado = next((usuario for usuario in usuarios if usuario['cpf'] == cpf.replace(".", "").replace("-", "")), None)

    elif opcao == "6":
        if not usuario_logado:
            print("Operação não permitida! Crie um usuário primeiro.")
            continue
        verificar_dados(usuario_logado['cpf'])

    elif opcao == "7":
        print("Obrigado por usar nossos serviços, tenha um ótimo dia.")
        break

    else:
        print("Opção inválida, por favor selecione uma das opções:")
