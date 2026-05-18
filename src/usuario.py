import networkx as nx
import matplotlib.pyplot as plt
from typing import cast
import pickle

class Usuario:
    def __init__(self, nome:str, display:str, email:str, id:int):
        self.id:int = id
        self.nome:str = nome.title().strip()[:50]
        self.display_name:str = display.strip()[:30]
        self.email:str = email
        self.lista_amigos:list[Usuario] = []

    def adicionar_amizade(self, outro_usuario:Usuario) -> None:
        if outro_usuario == self:
            print("Você não pode adicionar a si mesmo.")
            return
        if outro_usuario in self.lista_amigos and self in outro_usuario.lista_amigos:
            print("Esse usuário já é seu amigo.")
            return
        self.lista_amigos.append(outro_usuario)
        outro_usuario.lista_amigos.append(self)
        print(f"{outro_usuario.nome} foi adicionado aos amigos.")

    def remover_amizade(self, outro_usuario:Usuario) -> None:
        if outro_usuario not in self.lista_amigos:
            print("Esse usuário não está na sua lista.")
            return
        self.lista_amigos.remove(outro_usuario)
        outro_usuario.lista_amigos.remove(self)

    def listar_amigos(self) -> None:
        if not self.lista_amigos:
            print("Você não possui amigos adicionados.")
            return
        print("\n~~~ LISTA DE AMIGOS ~~~")
        for amigo in self.lista_amigos:
            print(f"- {amigo.nome} ({amigo.email})")

    def listar_recomendacoes(self) -> None:
        print("\nplaceholder")

    def edit_nome(self, nome:str):
        nome = nome.capitalize().strip()
        if self.nome != nome:
            self.nome = nome
    def edit_email(self, email:str):
        email = email.strip()
        if self.email != email:
            self.email = email
    def edit_display(self, display:str):
        display = display.strip()
        if self.display_name.strip():
            self.display_name = display
    def show_usuario(self) -> None:
        print(f"Apelido: {self.display_name}")
        print(f"Nome Completo: {self.nome}")
        print(f"Email: {self.email}")
        print(f"ID: {self.id}")
        print("Amigos: ", end="")
        if self.lista_amigos:
            for x in range(len(self.lista_amigos)):
                if x == len(self.lista_amigos)-1:
                    print(f"{self.lista_amigos[x].display_name}")
                else:
                    print(f"{self.lista_amigos[x].display_name}, ", end="")
        else:
            print("n/a")

class Rede_Social:
    def __init__(self):
        self.graph: nx.Graph[int] = nx.Graph()
        self.next_id:int = 1
        self.path_json: str = "cache/save.pkl"

    def buscar_usuario_nome(self, nome: str) -> list[Usuario]|None:
        lista: list[Usuario] = []
        nome = nome.lower().strip()
        for x in self.graph.nodes(data=True):
            if nome in cast(Usuario, x[1]["usuario"]).nome: lista.append(cast(Usuario, x[1]["usuario"]))
        return lista

    def buscar_usuario_email(self, email: str) -> Usuario|None:
        email = email.strip()
        for x in self.graph.nodes(data=True):
            if email == cast(Usuario, x[1]["usuario"]).email:
                return cast(Usuario, x[1]["usuario"])
        return None

    def buscar_usuario_id(self, id: int) -> Usuario|None:
        if self.graph.nodes[id]:
            return self.graph.nodes[id].get('usuario')
        return None

    def criar_usuario(self, nome:str, display:str, email:str) -> None:
        for x in self.graph.nodes(data=True):
            if cast(Usuario, x[1]["usuario"]).display_name == display:
                print("Já existe um usuário com esse nome")
                return
            if cast(Usuario, x[1]["usuario"]).email == email:
                print("Já existe um usuário com esse email")
                return
        self.graph.add_node(self.next_id, usuario=Usuario(nome, display, email, self.next_id))
        self.next_id += 1

    def remover_usuario(self, usuario:Usuario):
        if usuario.lista_amigos:
            for x in usuario.lista_amigos:
                if usuario in x.lista_amigos:
                    x.remover_amizade(usuario)
        self.graph.remove_node(usuario.id)

    def show_graph(self):
        labels = {node: data["usuario"].display_name for node, data in self.graph.nodes(data=True)}
        nx.draw_circular(self.graph, labels=labels, with_labels=True)
        plt.show()
        pass
    def fazer_amizade(self, usuario:Usuario, outro_usuario:Usuario) -> None:
        usuario.adicionar_amizade(outro_usuario)
        _= self.graph.add_edge(usuario.id, outro_usuario.id)
    def desfazer_amizade(self, usuario:Usuario, outro_usuario:Usuario) -> None:
        usuario.remover_amizade(outro_usuario)
        self.graph.remove_edge(usuario.id, outro_usuario.id)
    def salvar_json(self):
        with open(self.path_json, "wb") as file:
            pickle.dump(self, file)

'''
usuarios: list[Usuario] = []

def criar_usuario(nome:str, email:str):
    for usuario in usuarios:
        if usuario.email == email:
            print("Já existe um usuário com esse email.")
            return None
    novo_usuario = Usuario(nome, email)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso.")
    return novo_usuario

def procurar_usuario(email:str):
    for usuario in usuarios:
        if usuario.email == email:
            return usuario
    return None

def remover_usuario(email:str):
    usuario = procurar_usuario(email)
    if usuario is None:
        print("Usuário não encontrado.")
        return
    for amigo in usuario.lista_amigos:
        amigo.lista_amigos.remove(usuario)
    usuarios.remove(usuario)
    print("Usuário removido com sucesso.")

def atualizar_usuario(email:str, novo_nome:str|None = None, novo_email:str|None = None):
    usuario = procurar_usuario(email)
    if usuario is None:
        print("Usuário não encontrado.")
        return
    if novo_nome:
        usuario.nome = novo_nome
    if novo_email:
        usuario.email = novo_email
    print("Usuário atualizado com sucesso.")
'''
