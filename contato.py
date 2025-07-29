def adicionar_contato(contatos, nome, telefone, email):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        print(f"{indice}. {status} {contato['nome']} - Telefone: {contato['telefone']}, Email: {contato['email']}")
    return

def editar_contato(contatos, escolha, indice_contato, novo_nome, novo_telefone, novo_email):
    indice_contato_ajustado = int(indice_contato) - 1
    if escolha == "1":
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["nome"] = novo_nome
            print(f"Nome do contato {indice_contato} atualizado para {novo_nome}")
        else:
            print("Índice de contato não encontrado!")
    elif escolha == "2":
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["telefone"] = novo_telefone
            print(f"Telefone do contato {indice_contato} atualizado para {novo_telefone}")
        else:
            print("Índice de contato não encontrado!")
    elif escolha == "3":
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["email"] = novo_email
            print(f"Email do contato {indice_contato} atualizado para {novo_email}")
        else:
            print("Índice de contato não encontrado!")
    elif escolha == "4":
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["nome"] = novo_nome
            contatos[indice_contato_ajustado]["telefone"] = novo_telefone
            contatos[indice_contato_ajustado]["email"] = novo_email
            print(f"Contato {indice_contato} atualizado com sucesso!")
        else:
                print("Índice de contato não encontrado!")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if contatos[indice_contato_ajustado]["favorito"] == False:
            contatos[indice_contato_ajustado]["favorito"] = True
            print(f"Contato {indice_contato} marcado como favorito!")
        else:
            contatos[indice_contato_ajustado]["favorito"] = False
            print(f"Contato {indice_contato} desmarcado como favorito!")
    else:
        print("Índice de contato não encontrado!")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. {contato['nome']} - Telefone: {contato['telefone']}, Email: {contato['email']}")
    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print(f"Contato {indice_contato} apagado com sucesso!")
    else:
        print("Índice de contato não encontrado!")
    return

contatos = []
while True:
    print("\nMenu de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        ver_contatos(contatos)
        print("\nDigite qual dado deseja editar:")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        print("4. Todos os dados")
        escolha_editar = input("Digite a sua escolha: ")
        indice_contato = input("Digite o número do contato que deseja editar: ")
        if escolha_editar == "1":
            novo_nome = input("Digite o novo nome: ")
            editar_contato(contatos, escolha_editar, indice_contato, novo_nome, "", "")
        elif escolha_editar == "2":
            novo_telefone = input("Digite o novo telefone: ")
            editar_contato(contatos, escolha_editar, indice_contato, "", novo_telefone, "")
        elif escolha_editar == "3":
            novo_email = input("Digite o novo email: ")
            editar_contato(contatos, escolha_editar, indice_contato, "", "", novo_email)
        elif escolha_editar == "4":
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo email: ")
            editar_contato(contatos, escolha_editar, indice_contato, novo_nome, novo_telefone, novo_email)
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar ou desfavoritar: ")
        favoritar_contato(contatos, indice_contato)
    
    elif escolha == "5":
        ver_contatos_favoritos(contatos)
    
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)
        ver_contatos(contatos)
    
    elif escolha == "7":
        print("Saindo do gerenciador de contatos...")
        break

    print("Programa encerrado. Até logo!")