from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List

app = FastAPI()

# Configuração do banco de dados
db_config = {
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'mysql',  # Nome do serviço no docker-compose
    'port': 3306,
    'database': 'mydatabase'
}

# Modelo de dados para a requisição
class Atividade(BaseModel):
    nome: str
    idade: int
    sexo: str

# Conexão com o banco de dados
def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Rota para inserir dados na tabela
@app.post("/adicionar_atividade/", summary="Adicionar nova atividade", tags=["Atividades"])
def add_record(atividade: Atividade):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO tbalunos (nome, idade, sexo) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (atividade.nome, atividade.idade, atividade.sexo))
        connection.commit()

        return {"message": "Registro inserido com sucesso!", "data": atividade.dict()}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao inserir o registro")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Rota para buscar todos os registros
@app.get("/pegar_todas_atividades/", summary="Obter todas as atividades", tags=["Atividades"])
def get_all_records():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        select_query = "SELECT * FROM tbalunos"
        cursor.execute(select_query)
        records = cursor.fetchall()

        return {"data": records}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao buscar os registros")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Rota para buscar um registro por ID
@app.get("/pegar_uma_atividade/{id}", summary="Obter atividade por ID", tags=["Atividades"])
def get_record(id: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        select_query = "SELECT * FROM tbalunos WHERE id = %s"
        cursor.execute(select_query, (id,))
        record = cursor.fetchone()

        if not record:
            raise HTTPException(status_code=404, detail="Registro não encontrado")

        return {"data": record}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao buscar o registro")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Rota para atualizar um registro existente por ID
@app.put("/atualizar_atividade/{id}", summary="Atualizar atividade por ID", tags=["Atividades"])
def update_record(id: int, atividade: Atividade):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        update_query = "UPDATE tbalunos SET nome = %s, idade = %s, sexo = %s WHERE id = %s"
        cursor.execute(update_query, (atividade.nome, atividade.idade, atividade.sexo, id))
        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Registro não encontrado")

        return {"message": "Registro atualizado com sucesso!", "data": atividade.dict()}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao atualizar o registro")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Rota para deletar um registro por ID
@app.delete("/deletar_atividade/{id}", summary="Deletar atividade por ID", tags=["Atividades"])
def delete_record(id: int):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM tbalunos WHERE id = %s"
        cursor.execute(delete_query, (id,))
        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Registro não encontrado")

        return {"message": "Registro deletado com sucesso!"}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Erro ao deletar o registro")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Inicializando o servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
