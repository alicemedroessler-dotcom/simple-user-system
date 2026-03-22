usuarios = []


def mostrar_menu():
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Editar usuário")
    print("4 - Remover usuário")
    print("5 - Sair")


def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    idade = input("Digite a idade: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    if not idade.isdigit():
        print("Idade inválida.")
        return

    usuario = {
        "nome": nome,
        "idade": int(idade)
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    print("\nLista de usuários:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. {usuario['nome']} - {usuario['idade']} anos")


def editar_usuario():
    if not usuarios:
        print("Nenhum usuário para editar.")
        return

    listar_usuarios()
    indice = input("Digite o número do usuário que deseja editar: ").strip()

    if not indice.isdigit():
        print("Valor inválido.")
        return

    indice = int(indice)

    if indice < 1 or indice > len(usuarios):
        print("Usuário não encontrado.")
        return

    usuario = usuarios[indice - 1]

    novo_nome = input(f"Novo nome ({usuario['nome']}): ").strip()
    nova_idade = input(f"Nova idade ({usuario['idade']}): ").strip()

    if novo_nome:
        usuario["nome"] = novo_nome

    if nova_idade.isdigit():
        usuario["idade"] = int(nova_idade)

    print("Usuário atualizado com sucesso!")


def remover_usuario():
    if not usuarios:
        print("Nenhum usuário para remover.")
        return

    listar_usuarios()
    indice = input("Digite o número do usuário que deseja remover: ").strip()

    if not indice.isdigit():
        print("Valor inválido.")
        return

    indice = int(indice)

    if indice < 1 or indice > len(usuarios):
        print("Usuário não encontrado.")
        return

    removido = usuarios.pop(indice - 1)
    print(f"Usuário {removido['nome']} removido com sucesso!")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            remover_usuario()
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()