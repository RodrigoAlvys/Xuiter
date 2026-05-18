import os
import pickle
from src.usuario import *

if os.path.exists("cache/save.pkl"):
    with open("cache/save.pkl", "rb") as file:
        teste: Rede_Social = pickle.load(file)
else:
    teste = Rede_Social()

while True:
    print("""
    1 - criar node
    2 - remover node
    3 - criar edge
    4 - mostrar grafico
    5 - recomendações
    6 - exit
        """)
    opc = input("-> ")
 
    if opc == '1':
        teste.criar_usuario(input("nome: "), input("display: "), input("email: "))
        teste.salvar_json()
    elif opc == '2':
        remover = teste.buscar_usuario_id(int(input("id: ")))
        if remover is not None:
            teste.remover_usuario(remover)
            teste.salvar_json()
    elif opc == '3':
        usuario = teste.buscar_usuario_id(int(input("id: ")))
        outro_usuario = teste.buscar_usuario_id(int(input("id: ")))
        if usuario is not None and outro_usuario is not None:
            teste.fazer_amizade(usuario, outro_usuario)
            teste.salvar_json()
    elif opc == '4':
        teste.show_graph()

    elif opc == '5':
        usuario = teste.buscar_usuario_id(
            int(input("id: "))
        )
        if usuario is not None:
            usuario.listar_recomendacoes(teste)

    if opc == '6':
        break

