from usuario import *

def entrar_usuario():

    print("\n~~~ ENTRAR ~~~")
    email = input("Digite seu email: ")
    usuario = procurar_usuario(email)
    if usuario is None:
        print("Usuário não encontrado.")
        return
    menu_usuario(usuario)

def menu_usuario(usuario):
    while True:
        print(f"\n~~~ LOGADO COMO {usuario.nome} ~~~")
        print("1 - Olhar lista de amizades")
        print("2 - Olhar recomendações")
        print("3 - Adicionar amizade")
        print("4 - Remover amizade")
        print("5 - Sair da conta")

        escolha = input("Escolha: ")
        if escolha == "1":
            usuario.listar_amigos()
        elif escolha == "2":
            usuario.listar_recomendacoes()
        elif escolha == "3":
            adicionar_amizade(usuario)
        elif escolha == "4":
            remover_amizade(usuario)
        elif escolha == "5":
            break
        else:
            print("Opção inválida.")


def adicionar_amizade(usuario):
    print("\n~~~ ADICIONAR AMIZADE ~~~")
    email = input("Email do usuário: ")
    outro_usuario = procurar_usuario(email)
    if outro_usuario is None:
        print("Usuário não encontrado.")
        return
    usuario.adicionar_amizade(outro_usuario)


def remover_amizade(usuario):
    print("\n~~~ REMOVER AMIZADE ~~~")
    email = input("Email do usuário: ")
    outro_usuario = procurar_usuario(email)
    if outro_usuario is None:
        print("Usuário não encontrado.")
        return
    usuario.remover_amizade(outro_usuario)


while True:

    print("\n~~~ XUITER ~~~")
    print("1 - Criar usuário")
    print("2 - Remover usuário")
    print("3 - Atualizar usuário")
    print("4 - Entrar como usuário")
    print("5 - Finalizar programa")
    opcao = input("Escolha: ")

    if opcao == "1":
        print("\n~~~ CRIAR USUÁRIO ~~~")

        nome = input("Nome: ")
        email = input("Email: ")

        criar_usuario(nome, email)

    elif opcao == "2":
        print("\n~~~ REMOVER USUÁRIO ~~~")
        email = input("Digite o email do usuário: ")
        remover_usuario(email)

    elif opcao == "3":
        print("\n~~~ ATUALIZAR USUÁRIO ~~~")
        email = input("Email atual do usuário: ")
        novo_nome = input("Novo nome (ENTER para manter): ")
        novo_email = input("Novo email (ENTER para manter): ")
        if novo_nome == "":
            novo_nome = None
        if novo_email == "":
            novo_email = None
        atualizar_usuario(email, novo_nome, novo_email)

    elif opcao == "4":
        entrar_usuario()

    elif opcao == "5":
        print("Programa encerrado.")
        break
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")