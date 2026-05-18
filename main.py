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
5 - exit
      """)
    opc = input("-> ")
    if opc == '5':
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
        usuario = teste.buscar_usuario_id(int(input("id: ")))
        outro_usuario = teste.buscar_usuario_id(int(input("id: ")))
        if usuario and outro_usuario is not None:
            teste.fazer_amizade(usuario, outro_usuario)
            teste.salvar_binario(save_path)
    elif opc == '4':
        teste.show_graph()


