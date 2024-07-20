class Task:
    def __init__(self, title, description, priority=3):
        self.title = title
        self.description = description
        self.priority = priority

    def __str__(self):
        return f'Titulo: {self.title}, DEscrição: {self.description}, Prioridade: {self.priority}'

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority=3):
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority)
        print(f'Tarefa "{title}" adicionada com sucesso!')

    def edit_task(self, index, title=None, description=None, priority=None):
        if 0 <= index < len(self.tasks):
            if title:
                self.tasks[index].title = title
            if description:
                self.tasks[index].description = description
            if priority is not None:
                self.tasks[index].priority = priority
            self.tasks.sort(key=lambda x: x.priority)
            print(f'Tarefa {index} editada com sucesso.')
        else:
            print('Texto invalido para a Tarefa.')

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Tarefa "{removed_task.title}" deletada com sucesso.')
        else:
            print('Texto invalido para a Tarefa.')

    def display_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                print(f'{i}. {task}')
        else:
            print('Tarefa não encontrada.')

def main():
    todo_list = ToDoList()

    while True:
        print("\n Menu:")
        print("1. Adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Deletar tarefa")
        print("4. Exibir tarefa")
        print("5. Sair")
        
        choice = input("Digite a sua escolha: ")

        if choice == '1':
            title = input("Titulo da tarefa: ")
            description = input("Descrição: ")
            priority = int(input("Prioridade (1 a 5): "))
            todo_list.add_task(title, description, priority)
        elif choice == '2':
            todo_list.display_tasks()
            index = int(input("Titulo da tarefa para editar: "))
            title = input("Novo titulo da tarefa: ")
            description = input("Nova descrição: ")
            priority = input("Nova prioridade (1 a 5): ")
            todo_list.edit_task(index, title or None, description or None, int(priority) if priority else None)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Titulo da tarefa para ser deletado: "))
            todo_list.delete_task(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Texto não encontrado. Tente novamente")

if __name__ == "__main__":
    main()
