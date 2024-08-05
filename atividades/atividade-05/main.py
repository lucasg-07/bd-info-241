import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Funções fornecidas e novas funções
def create_task(description):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()

def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        completed INTEGER NOT NULL)''')
    conn.commit()

# Menu principal
def main():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Excluir tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            description = input("Digite a descrição da tarefa: ")
            create_task(description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_id = int(input("Digite o ID da tarefa a ser marcada como concluída: "))
            mark_completed(task_id)
        elif choice == '4':
            task_id = int(input("Digite o ID da tarefa a ser excluída: "))
            delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()
