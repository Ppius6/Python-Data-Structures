# Task Manager Program
# This program allows users to add, view, edit, and delete tasks. Each task has a name, description, deadline, and priority.

# Initialize an empty list called 'tasks' to store tasks.
tasks = []

def addTask(taskName, taskDescription, taskDeadline, taskPriority):
    """
    Adds a new task to the tasks list.
    
    Parameters:
    - taskName: Name of the task
    - taskDescription: A brief description of the task
    - taskDeadline: The deadline for completing the task
    - taskPriority: Priority of the task (High, Medium, Low)
    
    Returns:
    - A confirmation message after adding the task.
    """
    
    # Create a dictionary representing the task with the provided details.
    task = {
        'name': taskName,
        'description': taskDescription,
        'deadline': taskDeadline,
        'priority': taskPriority
    }
    
    # Add the task dictionary to the tasks list.
    tasks.append(task)
    
    # This program assumes tasks are stored in memory for simplicity.
    
    return "Task added successfully!"

def viewTasks(priorityFilter=None):
    """
    Displays tasks based on the given priority filter.
    
    Parameters:
    - priorityFilter: The priority to filter tasks by. If not provided, all tasks are displayed.
    
    Returns:
    - A list of tasks that match the filter criteria.
    """
    
    # If a priority filter is provided, filter tasks based on that priority.
    if priorityFilter:
        filtered_tasks = [task for task in tasks if task['priority'] == priorityFilter]
        return filtered_tasks
    else:
        # If no filter is provided, return all tasks.
        return tasks

def main():
    """
    Main function to run the Task Manager program. It displays a menu for users to select options and performs the corresponding actions.
    """
    
    while True:
        # Display menu options to the user.
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        # Get user's choice.
        choice = input("Please select an option: ")
        
        # Perform actions based on user's choice.
        if choice == '1':
            # Get task details from the user.
            taskName = input("Enter task name: ")
            taskDescription = input("Enter task description: ")
            taskDeadline = input("Enter task deadline (e.g., October 11, 2023, 6:00 AM): ")
            taskPriority = input("Enter task priority (High, Medium, Low): ")
            
            # Add the task using the provided details.
            result = addTask(taskName, taskDescription, taskDeadline, taskPriority)
            print(result)
            
        elif choice == '2':
            # Ask user if they want to filter tasks by priority.
            filterChoice = input("Do you want to filter tasks by priority? (yes/no) ")
            
            if filterChoice.lower() == 'yes':
                priorityFilter = input("Enter priority to filter by (High, Medium, Low): ")
                filtered_tasks = viewTasks(priorityFilter)
                
                # Display the filtered tasks.
                print("\nTasks with priority", priorityFilter)
                for task in filtered_tasks:
                    print(task)
            else:
                # Display all tasks.
                all_tasks = viewTasks()
                print("\nAll Tasks")
                for task in all_tasks:
                    print(task)
                    
        elif choice == '3':
            # Exit the program.
            print("Thank you for using Task Manager!")
            break
        else:
            # If user selects an invalid option.
            print("Invalid choice. Please select a valid option.")

# Start the Task Manager program by calling the main function.
if __name__ == "__main__":
    main()
