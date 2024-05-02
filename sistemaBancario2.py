def fazerDeposito(saldo,valor,extrato,/):
    saldo += valor
    extrato+= f"Depósito: R$ {valor:.2f}\n"
    return saldo,valor,extrato

def fazerSaque(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            return saldo,''
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            return saldo,''
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            return saldo,''
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            return saldo , extrato
        else:
            print("Operação falhou! O valor informado é inválido.")
            return saldo,''

def exibirExtrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def cadastrsarEndereco(logradouro,numero, bairro, cidade,estado):
    endereco=f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    return endereco

def cadastrarCliente(usuarios,nome,cpf,dataDeNascimento,endereco):
    if cpf not in usuarios:
        usuarios[cpf]={"Nome":nome,"CPF":cpf,"Data De Nascimento":dataDeNascimento,"Endereco":endereco}
        return usuarios
    else:
            print("Usuário já cadastrado")

def listarContas(listaContas):
    if listaContas:
        for index, conta in enumerate(listaContas):
            print(conta)
    else:
        print("Lista Vazia")

def vincularUsuario(cpf,contas):
    teste=False
    for chave, valor in usuarios.items():
                if cpf==chave:
                    usuarioVinculado=usuarios[chave]
                    teste=True
    if teste:
        if contas:
            for index, conta in enumerate(contas):
                nConta=index+2
        else:
            nConta=1
        return nConta,usuarioVinculado
    else:
        print("Operação inválida, nenhum usuário com o CPF cadastrado.")  

def cadastrarConta(cpf,conta,contas):
    if usuarios:
        agencia= "001"
        teste=False
        for chave, valor in usuarios.items():
            if cpf==chave:
                usuarioVinculado=usuarios[chave]
                teste=True
        if teste:
            if contas:
                for index, conta in enumerate(contas):
                    nConta=index+2
            else:
                nConta=1
            conta[nConta]={"Agencia":agencia,"Numero de conta":nConta,"Usuário":usuarioVinculado}
            contas.append(conta)
            return conta,contas
        else:
            print("Operação inválida, nenhum usuário com o CPF cadastrado.")  
    else:
        print("Operação inválida, nenhum usuário cadastrado.")
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios={}
conta={}
listaContas=[]
menuMetodos = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar conta de usuário
[b] Criar conta bancãria
[lc] Listar Contas
[q] Sair
=> """



while True:
    opcao = input(menuMetodos)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo,valor,extrato=fazerDeposito(saldo,valor,extrato)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        saldo,extrato=fazerSaque(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
        numero_saques += 1
    
    elif opcao == "e":
        exibirExtrato(saldo,extrato=extrato)

    elif opcao == "u":
        nome=str(input("Digite seu nome:"))
        cpf=int(input("Digite seu CPF:"))
        dataDeNascimento=int(input("Digite sua data de nascimento:"))
        print("Endereço:")
        logradouro=str(input("Digite seu logradouro:"))
        numero=int(input("Digite seu numero:"))
        bairro=str(input("Digite seu bairro:"))
        cidade=str(input("Digite sua cidade:"))
        estado=str(input("Digite a sigla do seu estado:"))
        
        cadastrarCliente(usuarios=usuarios,cpf=cpf,nome=nome,dataDeNascimento=dataDeNascimento,endereco=cadastrsarEndereco(logradouro=logradouro,numero=numero,bairro=bairro,cidade=cidade,estado=estado))
        

    elif opcao =="b":
            cpf=int(input("Digite seu CPF:"))
            cadastrarConta(cpf=cpf,conta=conta,contas=listaContas)
    
    elif opcao == "lc":
        listarContas(listaContas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")