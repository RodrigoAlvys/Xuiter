class Usuario:
    contador_id: int = 0
    def __init__(self, nome:str, email:str):
        self.id: int = Usuario.contador_id
        Usuario.contador_id += 1
        self.nome: str = nome
        self.email: str = email
        self.lista_amigos: list[Usuario] = []

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
        print(f"{outro_usuario.nome} foi removido dos amigos.")

    def listar_amigos(self) -> None:
        if not self.lista_amigos:
            print("Você não possui amigos adicionados.")
            return
        print("\n~~~ LISTA DE AMIGOS ~~~")
        for amigo in self.lista_amigos:
            print(f"- {amigo.nome} ({amigo.email})")

    def listar_recomendacoes(self) -> None:
        print("\nplaceholder")

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
