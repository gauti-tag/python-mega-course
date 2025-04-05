def get_todos(filepath):
    with open(filepath, 'r') as file_content_local:
        todos_local = file_content_local.readlines()
    return todos_local


def write_todos(filpath, todos_arg):
    with open(filpath, 'w') as file_content_local:
        file_content_local.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ").strip()
  
    # Check if user action is "add"
    if user_action.startswith("add"): 
        todo = user_action[4:]
        #Fetch the existing todos list        
        
        todos = get_todos('todo/todos.txt')
        
        todos.append(todo + '\n')
        
        write_todos('todo/todos.txt', todos)
            
    elif user_action.startswith("show"):
        #Fetch data from file    
        todos = get_todos('todo/todos.txt')
        
        # Enumerate function generate indexing for a list
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"Todo n°{index + 1}: {item.title()}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos('todo/todos.txt')
                
            new_todo = input("Enter new todo: ")
            todos[number] =  new_todo + "\n"
            
            write_todos('todo/todos.txt', todos)
    
        except ValueError:
            print('Your command is not valid')
            continue
            
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = get_todos('todo/todos.txt')
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos('todo/todos.txt', todos)
                
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
    
