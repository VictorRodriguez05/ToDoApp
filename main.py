from task_model import TaskModel

def main():
    task = TaskModel("estudiar para el examen")
    print(f"Tarea desde estudiante3: {task.get_task_name()}")
    task.set_done()
    print("Estudiante3 completó la tarea")

if __name__ == "__main__":
    main()
