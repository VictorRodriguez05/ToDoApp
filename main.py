from task_model import TaskModel

def main():
    task = TaskModel("estudiar para el examen")
    print(f"tarea creada: {task.get_task_name()}")



if __name__ == "__name__":
   main()   