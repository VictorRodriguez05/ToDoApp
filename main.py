from task_model import TaskModel

def main():
    task = TaskModel("estudiar para el examen")
    print(f"tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada:  {task.is_completdC}")



if __name__ == "__name__":
   main()   