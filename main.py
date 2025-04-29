from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.connection_db import init_db


@asynccontextmanager
async def lifespan(app:FastAPI):
    await init_db()
    yield
app = FastAPI(lifespan=lifespan)

usuario: List[Usuario] = cargar_usuario_csv()

@app.get("/")
async def inicio():
    return {"mensaje": "API DE USUARIOS ACTIVA"}

# Crear  o adicionar usuarios
@app.post("/usuarios", response_model=Usuario)
async def crear_usuario(usuario: Usuario):
    if any(p.id == usuario.id for p in usuario):
        raise HTTPException(status_code=400, detail="El ID del usuario ya existe")
    usuario.append(usuario)
    guardar_usuario_csv(usuario)
    return usuario
#consultar todos los usuarios
@app.get("/usuario", response_model=List[UsuarioRespuesta])
async def listar_usuario():
    return listar_usuario

# Consultar un solo usuario
@app.get("/usuario/buscar/{nombre}", response_model=List[Usuario])
async def buscar_por_nombre(nombre: str):
    return [p for p in usuario if nombre.lower() in p.nombre.lower()]



#actualizar estado del usuario
@app.patch("/usuario/{usuario_id}", response_model=List[Usuario]
async def update_pet(usuario_id:int, usuario_update:usuario,session:Session=Depends(get_session)):
    usuario = await crud.update_usuario(session, usuario_id, usuario_update.dict(exclude_unset=True))
    if pet is None:
    return usuario

#Hacer usuario premium



#consultar usuarios activos
@app.get("/allusuarios", response_model=list[UsuarioWithId])
async def show_all_usuarios():
    usuarios=read_all_usuarios()
    return usuarios

    '''return [
        {
            "id":1,
            "name":"Helen",
        },
        {
           "id":1,
            "name":"Daniel",
        },
        {
            "id":3,
            "name":"Karoslay",
        }
    ]'''


