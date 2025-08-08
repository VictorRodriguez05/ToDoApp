from task_model import TaskModel

def main():
    task = TaskModel("hacer tarea")
    print(f"Tarea: {task.get_task_name()}")
    task.set_done()
    print("Tarea marcada como hecha")

if __name__ == "__main__":
    main()
