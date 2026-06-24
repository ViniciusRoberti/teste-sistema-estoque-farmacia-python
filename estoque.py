#Definimos a variavel estoque como vazio.
estoque = {}

#Em seguida criamos nosso menu de escolha do usuário.
while True: 
    print("\n========== CONTROLE DE ESTOQUE ==========")
    print("Escolha a opção:")
    print("1 - Cadastrar medicamento.")
    print("2 - Checar estoque.")
    print("3 - Verificar estoque baixo")
    print("4 - Remover medicamento.")
    print("5 - Atualizar estoque.")
    print("6 - Sair")
    opcao = input("Entre apenas com o numero da opção: ")

#Começamos a desenvolver as opções escolhidas pelo usuário.
    #Opção 1
    if opcao == "1":
        nome = input("\nEntre com o nome do medicamento: ")
        quantidade = int(input(f"Entre com a quantidade de {nome}: "))
        print(f"Cadastrado um total de {quantidade} {nome} no estoque.")
        estoque[nome] = quantidade

    #Opção 2
    elif opcao == "2":
        if not estoque:
            print("Estoque vazio.")
        else:
            print("\n====== ESTOQUE ATUAL ======")
            for produto, qtd in estoque.items():
                print(f"{produto} - {qtd} unidades.")

    #Opção 3
    elif opcao == "3":
        if not estoque:
            print("Estoque vazio.")
        else:
            estoque_baixo = False
            print("\n====== VERIFICAÇÃO DE ESTOQUE ======")
            for produto, qtd in estoque.items():
                if qtd <= 10: 
                    estoque_baixo = True
                    print(f"{produto} está com o estoque em pouca quantidade")
            if not estoque_baixo:
                print("\nEstoque OK")
    
    #Opção 4
    elif opcao == "4": 
        nome = input("Qual medicamento remover? ")
        if nome in estoque:
            del estoque[nome]
            print(f"\n === O medicamento {nome} foi removido do estoque. ===")
        else:
            print(f"\n === Medicamento não encontrado. === ")

    #Opção 5
    elif opcao == "5":
        nome = input("Qual medicamento terá a quantidade atualizada no estoque? ")
        if nome in estoque:
            nova_quantidade = int(input(f"Entre com a quantidade de {nome}: "))
            estoque[nome] = nova_quantidade
            print(f"A quantidade de {nome} foi atualizada para {nova_quantidade}.")
        else:
            print("\n === Medicamento não encontrado. === ")

    #Opção 6
    elif opcao == "6":
        print("Sistema encerrado")
        break

    #Caso a opção do usuário seja diferente de uma disponivel no menu.
    else:
        print("\nOpção inválida.")

