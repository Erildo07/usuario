carrinho = []

while True:
    print("\n1. Adicionar item")
    print("2. Ver carrinho")
    print("3. Finalizar compra")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Nome do item: ")
        carrinho.append(item)
        print(f"{item} adicionado ao carrinho.")

    elif opcao == "2":
        if not carrinho:
            print("Carrinho vazio.")
        else:
            print("\nItens no carrinho:")
            for item in carrinho:
                print("-", item)

    elif opcao == "3":
        if not carrinho:
            print("Carrinho vazio. Nenhuma compra finalizada.")
        else:
            print("\nCompra finalizada com os itens:")
            for item in carrinho:
                print("-", item)
            carrinho = []

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")