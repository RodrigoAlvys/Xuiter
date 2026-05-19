import pickle
from src.usuario import *

save_path:str = "cache/save.pkl"
with open(save_path, "rb") as file:
    teste:Rede_Social = pickle.load(file)
while True:
    print("""
1 - criar node
2 - remover node
3 - criar edge
4 - mostrar grafico
5 - mostrar todos usuários
6 - Editar Usuario
7 - Recomendado
8 - exit
      """)
    opc = input("-> ")
    if opc == '8':
        break
    elif opc == '1':
        teste.criar_usuario(input("nome: "), input("display: "), input("email: "))
        teste.salvar_binario(save_path)
    elif opc == '2':
        remover = teste.buscar_usuario_id(int(input("id: ")))
        if remover is not None:
            teste.remover_usuario(remover)
            teste.salvar_binario(save_path)
    elif opc == '3':
        teste.mostrar_todos_usuarios()
        usuario = teste.buscar_usuario_id(int(input("id: ")))
        outro_usuario = teste.buscar_usuario_id(int(input("id: ")))
        if usuario and outro_usuario is not None:
            teste.fazer_amizade(usuario, outro_usuario)
            teste.salvar_binario(save_path)
    elif opc == '4':
        teste.show_graph()
    elif opc == '5':
        teste.mostrar_todos_usuarios()
    elif opc == '6':
        print("Qual usuário deseja modificar\nprocurar por:")
        print("1 - ")
        pass
    elif opc == '7':
        teste.mostrar_todos_usuarios()
        id:int = int(input("Digite um id -> "))
        user = teste.buscar_usuario_id(id)
        if user is not None:
            recomendados = teste.Lista_de_recomendados(user)
            if recomendados:
                for x in recomendados:
                    print(f"\n{x.id} - {x.display_name}")
                    y:str = input("Você deseja fazer amizade com esse usuario?").strip().lower()
                    if y == "sim":
                        teste.fazer_amizade(user, x)

        else:
            print("Não foi possível encontrar esse usuário")

    else:
        print("Comando não reconhecido")


