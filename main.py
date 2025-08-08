from task_model import TaskModel

def main():
    task = TaskModel("estudiar para el examen")
    print(f"tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada:  {task.is_completdC}")
    task.remove_task()
    print(f"tarea eliminada:  {task.get_task_name()}")



if __name__ == "__name__":
   main()   