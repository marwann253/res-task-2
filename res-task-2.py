import os  # Needed to check if file exists

FILE_NAME = "tasks.txt"

def load_tasks():
    """
    Reads the 'tasks.txt' file and returns a list of tasks.
    Handles the case where the file doesn't exist yet.
    """
    tasks = []
    
    # TODO: Check if the file exists using os.path.exists(FILE_NAME)
    # If it doesn't exist, return the empty 'tasks' list immediately.
  
  
    if not os.path.exists(FILE_NAME):
        return tasks




    # TODO: Open the file in 'read' mode ('r')
    # Use the 'with open(...) as file:' syntax for safety.

    with open (FILE_NAME,"r") as file:
    
        # TODO: Loop through the lines in the file
        # Strip the newline character ('\n') from the end of the line
        # Append the clean task string to the 'tasks' list.
        
        for line in file:
            newline= line.strip()
            tasks.apend(newline)
    return tasks


def save_task(task):
    """
    Appends a SINGLE new task to the file.
    """
    # TODO: Open the file in 'append' mode ('a')
    # This allows us to add to the end without deleting existing content.
   
    with open (FILE_NAME,"a") as file:
          


        # TODO: Write the task to the file
        # IMPORTANT: Don't forget to add a newline character ("\n") 
        # so the next task goes on a new line!
        file.write("\n"+task)

        pass


 
def rewrite_file(tasks):
    """
    Overwrites the ENTIRE file with the current list of tasks.
    Used when we delete a task.
    """
    # TODO: Open the file in 'write' mode ('w')
    # Warning: 'w' mode wipes the file clean! This is what we want here.
    with open (FILE_NAME,"w") as file:
        # TODO: Loop through the 'tasks' list
        # Write each task to the file, adding the "\n" again.
        pass
    for line in tasks:
        file.write(tasks+"\n")



def view_tasks(tasks):
    """
    Prints the list of tasks with index numbers.
    """
    print("\n--- Your To-Do List ---")
    
    # TODO: Check if the list is empty
    if not tasks :
        print("Your to do list is empty")
    # TODO: Loop through tasks using enumerate() to get the index
    # Example: for index, task in enumerate(tasks, start=1):
    # Print format: "1. Buy Milk"
    for i, task in enumerate(tasks,start=1):
        print(f"{i}.{task.strip()}")

#chat gpt used here :\
    
    pass


def delete_task(tasks):
    """
    Displays tasks, asks user which number to delete, updates list and file.
    """
    view_tasks(tasks)
    
    # TODO: Ask user for the number to delete
    Num=print("Please enter the number you want to delete")
    
    # TODO: Validate input
    # 1. Is it a number?
    # 2. Is it a valid index (between 1 and len(tasks))?
    if not Num.isdigit():
        Num=("Please enter integers")
    if Num >= 1 or Num <= len(tasks) :
      
    
    # TODO: Remove the item from the 'tasks' list
    # pop() is useful here.
      tasks.pop(Num)
    
    # TODO: Sync changes to disk
    # Call the rewrite_file(tasks) function to save the new state.
    rewrite_file(tasks)
    print("Task deleted.")


# --- Main Execution ---

def main():
    # TODO: Load existing tasks from file into memory at start
    # current_tasks = load_tasks()
    current_tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            # TODO: Add to list AND call save_task()
            task=input("Enter the task")
            current_tasks.append(task+"\n")
            save_task()

            
        elif choice == '2':
            # TODO: Call view_tasks()
            view_tasks()
        
            pass
            
        elif choice == '3':
            # TODO: Call delete_task()
            delete_task()
            pass
            
        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()