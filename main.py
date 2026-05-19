import pickle
from src.usuario import *

save_path: str = "cache/save.pkl"

def carregar_dados() -> Rede_Social:
    """Carrega os dados do arquivo pickle ou cria uma nova rede social"""
    try:
        with open(save_path, "rb") as file:
            rede = pickle.load(file)
            print("Dados carregados com sucesso!")
            return rede
    except FileNotFoundError:
        print("Arquivo de save não encontrado. Criando nova rede social...")
        return Rede_Social()
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        print("Criando nova rede social...")
        return Rede_Social()

def salvar_dados(rede: Rede_Social) -> None:
    """Salva os dados no arquivo pickle"""
    try:
        rede.salvar_binario(save_path)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def obter_numero(mensagem: str, tipo: type = int) -> any:
    """Obtém um número do usuário com validação"""
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print(f"Por favor, digite um {tipo.__name__} válido.")

def exibir_menu_principal():
    """Exibe o menu principal"""
    print("\n" + "="*50)
    print("               REDE SOCIAL")
    print("="*50)
    print("1 - Criar novo usuário")
    print("2 - Remover usuário")
    print("3 - Fazer amizade")
    print("4 - Desfazer amizade")
    print("5 - Mostrar grafo")
    print("6 - Mostrar todos os usuários")
    print("7 - Mostrar detalhes de um usuário")
    print("8 - Editar usuário")
    print("9 - Sistema de recomendações")
    print("10 - Buscar usuário")
    print("11 - Listar amigos de um usuário")
    print("12 - Estatísticas da rede")
    print("0 - Sair e salvar")
    print("="*50)

def criar_usuario(rede: Rede_Social) -> None:
    """Cria um novo usuário"""
    print("\n--- CRIAR NOVO USUÁRIO ---")
    nome = input("Nome completo: ").strip()
    if not nome:
        print("Nome não pode estar vazio!")
        return

    display = input("Apelido/Display name: ").strip()
    if not display:
        print("Apelido não pode estar vazio!")
        return

    email = input("Email: ").strip()
    if not email:
        print("Email não pode estar vazio!")
        return

    rede.criar_usuario(nome, display, email)
    salvar_dados(rede)

def remover_usuario(rede: Rede_Social) -> None:
    """Remove um usuário"""
    print("\n--- REMOVER USUÁRIO ---")
    rede.mostrar_todos_usuarios()
    id_usuario = obter_numero("Digite o ID do usuário a ser removido: ")

    usuario = rede.buscar_usuario_id(id_usuario)
    if usuario:
        confirmacao = input(f"Tem certeza que deseja remover '{usuario.display_name}'? (s/n): ").lower()
        if confirmacao == 's':
            rede.remover_usuario(usuario)
            salvar_dados(rede)
            print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado!")

def fazer_amizade(rede: Rede_Social) -> None:
    """Faz amizade entre dois usuários"""
    print("\n--- FAZER AMIZADE ---")
    print("Usuários disponíveis:")
    rede.mostrar_todos_usuarios()

    id1 = obter_numero("Digite o ID do primeiro usuário: ")
    id2 = obter_numero("Digite o ID do segundo usuário: ")

    usuario1 = rede.buscar_usuario_id(id1)
    usuario2 = rede.buscar_usuario_id(id2)

    if usuario1 and usuario2:
        if usuario1 == usuario2:
            print("Não é possível fazer amizade consigo mesmo!")
        elif usuario2 in usuario1.lista_amigos:
            print("Esses usuários já são amigos!")
        else:
            rede.fazer_amizade(usuario1, usuario2)
            salvar_dados(rede)
    else:
        print("Um ou ambos os usuários não foram encontrados!")

def desfazer_amizade(rede: Rede_Social) -> None:
    """Desfaz amizade entre dois usuários"""
    print("\n--- DESFAZER AMIZADE ---")
    id1 = obter_numero("Digite o ID do primeiro usuário: ")
    id2 = obter_numero("Digite o ID do segundo usuário: ")

    usuario1 = rede.buscar_usuario_id(id1)
    usuario2 = rede.buscar_usuario_id(id2)

    if usuario1 and usuario2:
        if usuario2 in usuario1.lista_amigos:
            rede.desfazer_amizade(usuario1, usuario2)
            salvar_dados(rede)
            print("Amizade desfeita com sucesso!")
        else:
            print("Esses usuários não são amigos!")
    else:
        print("Um ou ambos os usuários não foram encontrados!")

def mostrar_detalhes_usuario(rede: Rede_Social) -> None:
    """Mostra detalhes de um usuário específico"""
    print("\n--- DETALHES DO USUÁRIO ---")
    rede.mostrar_todos_usuarios()
    id_usuario = obter_numero("Digite o ID do usuário: ")

    usuario = rede.buscar_usuario_id(id_usuario)
    if usuario:
        print("\n" + "="*40)
        usuario.show_usuario()
        print("="*40)
    else:
        print("Usuário não encontrado!")

def editar_usuario(rede: Rede_Social) -> None:
    """Edita os dados de um usuário"""
    print("\n--- EDITAR USUÁRIO ---")
    rede.mostrar_todos_usuarios()
    id_usuario = obter_numero("Digite o ID do usuário a ser editado: ")

    usuario = rede.buscar_usuario_id(id_usuario)
    if not usuario:
        print("Usuário não encontrado!")
        return

    print("\nO que deseja editar?")
    print("1 - Nome completo")
    print("2 - Apelido (Display name)")
    print("3 - Email")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        novo_nome = input(f"Nome atual: {usuario.nome}\nNovo nome: ").strip()
        if novo_nome:
            usuario.edit_nome(novo_nome)
            print("Nome atualizado com sucesso!")
    elif opcao == '2':
        novo_display = input(f"Apelido atual: {usuario.display_name}\nNovo apelido: ").strip()
        if novo_display:
            usuario.edit_display(novo_display)
            print("Apelido atualizado com sucesso!")
    elif opcao == '3':
        novo_email = input(f"Email atual: {usuario.email}\nNovo email: ").strip()
        if novo_email:
            usuario.edit_email(novo_email)
            print("Email atualizado com sucesso!")
    else:
        print("Opção inválida!")
        return

    salvar_dados(rede)

def sistema_recomendacoes(rede: Rede_Social) -> None:
    """Sistema de recomendações de amizades"""
    print("\n--- SISTEMA DE RECOMENDAÇÕES ---")
    rede.mostrar_todos_usuarios()
    id_usuario = obter_numero("Digite o ID do usuário para recomendações: ")

    usuario = rede.buscar_usuario_id(id_usuario)
    if not usuario:
        print("Usuário não encontrado!")
        return

    print(f"\nBuscando recomendações para {usuario.display_name}...")
    recomendados = rede.Lista_de_recomendados(usuario)

    if recomendados:
        print(f"\n{'='*50}")
        print(f"Encontramos {len(recomendados)} recomendação(ões):")
        print('='*50)

        for recomendado in recomendados:
            print(f"\nID: {recomendado.id}")
            print(f"Nome: {recomendado.nome}")
            print(f"Apelido: {recomendado.display_name}")
            print(f"Email: {recomendado.email}")
            print(f"Amigos em comum: {len([amigo for amigo in recomendado.lista_amigos if amigo in usuario.lista_amigos])}")

            resposta = input("\nDeseja fazer amizade com este usuário? (s/n): ").lower()
            if resposta == 's':
                rede.fazer_amizade(usuario, recomendado)
                salvar_dados(rede)
                print(f"Amizade feita com {recomendado.display_name}!")
    else:
        print("Nenhuma recomendação disponível no momento.")

def buscar_usuario(rede: Rede_Social) -> None:
    """Busca usuários por diferentes critérios"""
    print("\n--- BUSCAR USUÁRIO ---")
    print("Buscar por:")
    print("1 - ID")
    print("2 - Nome completo")
    print("3 - Apelido")
    print("4 - Email")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        id_usuario = obter_numero("Digite o ID: ")
        usuario = rede.buscar_usuario_id(id_usuario)
        if usuario:
            usuario.show_usuario()
        else:
            print("Usuário não encontrado!")

    elif opcao == '2':
        nome = input("Digite o nome (ou parte dele): ").strip()
        resultados = rede.buscar_usuario_nome(nome)
        if resultados:
            print(f"\nEncontrados {len(resultados)} resultado(s):")
            for usuario in resultados:
                print(f"ID: {usuario.id} - {usuario.display_name} ({usuario.nome})")
        else:
            print("Nenhum usuário encontrado!")

    elif opcao == '3':
        apelido = input("Digite o apelido (ou parte dele): ").strip()
        resultados = rede.buscar_usuario_display(apelido)
        if resultados:
            print(f"\nEncontrados {len(resultados)} resultado(s):")
            for usuario in resultados:
                print(f"ID: {usuario.id} - {usuario.display_name} ({usuario.nome})")
        else:
            print("Nenhum usuário encontrado!")

    elif opcao == '4':
        email = input("Digite o email completo: ").strip()
        usuario = rede.buscar_usuario_email(email)
        if usuario:
            usuario.show_usuario()
        else:
            print("Usuário não encontrado!")

    else:
        print("Opção inválida!")

def listar_amigos_usuario(rede: Rede_Social) -> None:
    """Lista os amigos de um usuário específico"""
    print("\n--- LISTAR AMIGOS ---")
    rede.mostrar_todos_usuarios()
    id_usuario = obter_numero("Digite o ID do usuário: ")

    usuario = rede.buscar_usuario_id(id_usuario)
    if usuario:
        print(f"\nAmigos de {usuario.display_name}:")
        usuario.listar_amigos()
    else:
        print("Usuário não encontrado!")

def mostrar_estatisticas(rede: Rede_Social) -> None:
    """Mostra estatísticas da rede social"""
    print("\n--- ESTATÍSTICAS DA REDE ---")
    num_usuarios = rede.graph.number_of_nodes()
    num_amizades = rede.graph.number_of_edges()

    print(f"Total de usuários: {num_usuarios}")
    print(f"Total de amizades: {num_amizades}")

    if num_usuarios > 0:
        grau_medio = (2 * num_amizades) / num_usuarios
        print(f"Grau médio da rede: {grau_medio:.2f}")

        if rede.graph.nodes:
            # Encontrar usuário com mais amigos
            max_amigos = 0
            usuario_popular = None

            for node_id in rede.graph.nodes():
                usuario = rede.buscar_usuario_id(node_id)
                if usuario and len(usuario.lista_amigos) > max_amigos:
                    max_amigos = len(usuario.lista_amigos)
                    usuario_popular = usuario

            if usuario_popular:
                print(f"\nUsuário mais popular: {usuario_popular.display_name}")
                print(f"Amigos: {max_amigos}")

def main():
    """Função principal do programa"""
    rede = carregar_dados()

    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '0':
            print("\nSalvando dados e saindo...")
            salvar_dados(rede)
            print("Até logo!")
            break

        elif opcao == '1':
            criar_usuario(rede)

        elif opcao == '2':
            remover_usuario(rede)

        elif opcao == '3':
            fazer_amizade(rede)

        elif opcao == '4':
            desfazer_amizade(rede)

        elif opcao == '5':
            print("\n--- MOSTRANDO GRAFO ---")
            try:
                rede.show_graph()
            except Exception as e:
                print(f"Erro ao mostrar grafo: {e}")
                print("Certifique-se de que há usuários na rede.")

        elif opcao == '6':
            print("\n--- TODOS OS USUÁRIOS ---")
            if rede.graph.number_of_nodes() == 0:
                print("Nenhum usuário cadastrado ainda!")
            else:
                rede.mostrar_todos_usuarios()

        elif opcao == '7':
            mostrar_detalhes_usuario(rede)

        elif opcao == '8':
            editar_usuario(rede)

        elif opcao == '9':
            sistema_recomendacoes(rede)

        elif opcao == '10':
            buscar_usuario(rede)

        elif opcao == '11':
            listar_amigos_usuario(rede)

        elif opcao == '12':
            mostrar_estatisticas(rede)

        else:
            print("Opção inválida! Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
