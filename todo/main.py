while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ").strip()
  
    # Check if user action is "add"
    if "add" in user_action: 
        todo = user_action[4:]
        #Fetch the existing todos list        
        with open('todo/todos.txt', 'r') as file_content:
            todos = file_content.readlines()
        
        todos.append(todo)
                    
        with open('todo/todos.txt', 'w') as file_content:
            file_content.writelines(todos)
            
    elif "show" in user_action:
        #Fetch data from file    
        with open('todo/todos.txt', 'r') as file_content:
            todos = file_content.readlines()
        
        # Enumerate function generate indexing for a list
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"Todo n°{index + 1}: {item.title()}")
    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1
        
        with open('todo/todos.txt', 'r') as file_content:
            todos = file_content.readlines()
            
        new_todo = input("Enter new todo: ")
        todos[number] =  new_todo + "\n"
        
        with open('todo/todos.txt', 'w') as file_content:
            file_content.writelines(todos)
            
    elif "complete" in user_action:
        number = int(user_action[9:])
        
        with open('todo/todos.txt', 'r') as file_content:
            todos = file_content.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        
        with open('todo/todos.txt', 'w') as file_content:
            file_content.writelines(todos)
            
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
        
    elif "exit" in user_action:
        break
    else:
        print("Command is not valid.")
    
print("Bye Bye !")
    
