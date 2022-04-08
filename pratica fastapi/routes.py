from bd import base_de_dados
from models import Usuario
from fastapi import APIRouter

usuario = APIRouter()

# Rota Raiz
@usuario.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Rota Get All
@usuario.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get Id
@usuario.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    
    return {"Status": 404, "Mensagem": "Não encontrou usuario"}

# Rota Insere
@usuario.post("/usuarios")
def insere_usuario(usuario: Usuario):
    # criar regras de negocio
    base_de_dados.append(usuario)
    return usuario
