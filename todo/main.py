while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    match user_action:
        case "add": 
            todo = input("Enter a todo: ") + "\n"
            #Fetch the existing todos list
            file_content = open('todo/todos.txt', 'r')
            todos = file_content.readlines()
            file_content.close()
            
            todos.append(todo)
            
            file_content = open('todo/todos.txt', 'w')
            file_content.writelines(todos)
            file_content.close()
        case "show" | "display":
            #Fetch data from file
            file_content = open('todo/todos.txt', 'r')
            todos = file_content.readlines()
            file_content.close
            
            #new_todos = []
            #for item in todos:
            #    new_todos.append(item.strip('\n'))
            
            # A list comprehension
            #new_todos = [item.strip('\n') for item in todos]
            
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
    
