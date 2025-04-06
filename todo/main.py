def get_todos(filepath = 'todo/todos.txt'):
    with open(filepath, 'r') as file_content_local:
        todos_local = file_content_local.readlines()
    return todos_local


def write_todos(todos_arg, filpath = 'todo/todos.txt'):
    with open(filpath, 'w') as file_content_local:
        file_content_local.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ").strip()
  
    # Check if user action is "add"
    if user_action.startswith("add"): 
        todo = user_action[4:]
        #Fetch the existing todos list        
        
        todos = get_todos()
        
        todos.append(todo + '\n')
        
        write_todos(todos)
            
    elif user_action.startswith("show"):
        #Fetch data from file    
        todos = get_todos()
        
        # Enumerate function generate indexing for a list
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"Todo n°{index + 1}: {item.title()}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos()
                
            new_todo = input("Enter new todo: ")
            todos[number] =  new_todo + "\n"
            
            write_todos(todos)
    
        except ValueError:
            print('Your command is not valid')
            continue
            
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = get_todos()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos(todos)
                
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue
        
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
    
print("Bye Bye !")
    
