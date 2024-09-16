import mysql.connector

# Configurações de conexão com o banco de dados
db_config = {
    'user': 'root',
    'password': 'rootpassword',
    'host': 'localhost',  # Nome do serviço no docker-compose
    'port': 3306,
    'database': 'atv10'
}

def get_db_connection():
    # Função para estabelecer a conexão com o banco de dados
    connection = mysql.connector.connect(**db_config)
    return connection

# Função principal
def listar_status_aprovacao():
    # Estabelece a conexão com o banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta para buscar informações da tabela de matrícula com aluno, professor e disciplina
    query = """
    SELECT A.NOME_ALUNO, D.NOME_DISCIPLINA, M.N1, M.N2, M.FALTAS
    FROM TB_MATRICULA M
    JOIN TB_ALUNO A ON M.ID_ALUNO = A.ID_ALUNO
    JOIN TB_DISCIPLINA D ON M.ID_DISCIPLINA = D.ID_DISCIPLINA;
    """
    
    # Executa a consulta
    cursor.execute(query)
    resultados = cursor.fetchall()

    # Verifica o status de aprovação
    for row in resultados:
        nome_aluno = row[0]
        nome_disciplina = row[1]
        n1 = row[2]
        n2 = row[3]
        faltas = row[4]

        # Calcula a média
        media = (n1 + n2) / 2

        # Verifica as condições de aprovação
        if media >= 7.0 and faltas <= 5:
            status = "Aprovado"
        else:
            status = "Reprovado"

        print(f"Aluno: {nome_aluno}, Disciplina: {nome_disciplina}, Média: {media:.2f}, Faltas: {faltas}, Status: {status}")

    # Fecha o cursor e a conexão
    cursor.close()
    conn.close()

# Chama a função para listar o status de aprovação dos alunos
listar_status_aprovacao()
