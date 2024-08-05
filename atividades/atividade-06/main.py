from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Definição da URL do banco de dados SQLite
DATABASE_URL = "sqlite:///./dbalunos.db"

# Configuração do banco de dados e metadados
database = Database(DATABASE_URL)
metadata = MetaData()

# Definição da tabela de alunos
alunos = Table(
    "TB_ALUNO",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("aluno_nome", String(50)),
    Column("endereco", String(100)),
)

# Criação do motor do banco de dados e das tabelas
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# Definição do modelo Pydantic para criação e resposta de Alunos
class AlunoCreate(BaseModel):
    aluno_nome: str
    endereco: str

class Aluno(BaseModel):
    id: int
    aluno_nome: str
    endereco: str

    class Config:
        orm_mode = True

# Instância do FastAPI
app = FastAPI()

# Conectar e desconectar do banco de dados
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Rotas CRUD para Alunos

@app.post("/alunos/", response_model=Aluno)
async def criar_aluno(aluno: AlunoCreate):
    query = alunos.insert().values(aluno_nome=aluno.aluno_nome, endereco=aluno.endereco)
    last_record_id = await database.execute(query)
    return {**aluno.dict(), "id": last_record_id}

@app.get("/alunos/", response_model=list[Aluno])
async def listar_alunos():
    query = alunos.select()
    return await database.fetch_all(query)

@app.get("/alunos/{id}", response_model=Aluno)
async def listar_um_aluno(id: int):
    query = alunos.select().where(alunos.c.id == id)
    aluno = await database.fetch_one(query)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@app.put("/alunos/{id}", response_model=Aluno)
async def atualizar_aluno(id: int, aluno: AlunoCreate):
    query = alunos.update().where(alunos.c.id == id).values(aluno_nome=aluno.aluno_nome, endereco=aluno.endereco)
    await database.execute(query)
    return {**aluno.dict(), "id": id}

@app.delete("/alunos/{id}")
async def excluir_aluno(id: int):
    query = alunos.delete().where(alunos.c.id == id)
    result = await database.execute(query)
    if result:
        return {"message": "Aluno excluído com sucesso"}
    else:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

# Rota para a raiz
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application"}

# Servir arquivos estáticos e favicon
