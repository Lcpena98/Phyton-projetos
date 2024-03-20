menu=("""
        ========== MENU ==========
            1 - Depositar
            2 - Sacar
            3 - Extrato
            0 - Sair
        ==========================

    ==>
    """)
saldo = 0
limite = 500
extrato=""""""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao=int(input(menu))
    if opcao == 1:
        valor = float(input("Selecione o valor para depositar"))
        if valor >= 0:
            saldo += valor
            print(f"Valor de R${valor:10.2f} depositado com sucesso")
            extrato+= (f"""Valor de R${valor:10.2f} depositado
""")
        else:
            print("Valor inválido")

    elif opcao == 2:
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Selecione o valor para sacar"))
            if valor >= 0 and valor <=500 and valor<=saldo:
                saldo -= valor
                print(f"Valor de R${valor:10.2f} sacado com sucesso")
                numero_saques += 1
                extrato+= (f"""Valor de R${valor:10.2f} sacado
""")   
            else:
                print("SAQUE INVÁLIDO: Valor inválido")  
        else:
            print("SAQUE INVÁLIDO: Limite de saques diários já alcançado")  
    elif opcao == 3:
        print(f"""{extrato}
        
        Saldo atual = R${saldo:10.2f}""")
    elif opcao == 0:
        break
    else:
        print("Opção Inválida")