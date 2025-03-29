while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    match user_action:
        # Check if user action is "add"
        case "add": 
            todo = input("Enter a todo: ") + "\n"
            #Fetch the existing todos list        
            with open('todo/todos.txt', 'r') as file_content:
                todos = file_content.readlines()
            
            todos.append(todo)
                        
            with open('todo/todos.txt', 'w') as file_content:
                file_content.writelines(todos)
                
        case "show" | "display":
            #Fetch data from file    
            with open('todo/todos.txt', 'r') as file_content:
                todos = file_content.readlines()
            
            # Enumerate function generate indexing for a list
            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"Todo n°{index + 1}: {item.title()}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] =  new_todo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case whatever:
            print('Hey ! you entered an unknown command')
    
print("Bye Bye !")
    
