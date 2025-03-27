
todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    match user_action:
        case "add": 
            user = input("Enter a todo: ")
            todos.append(user)
        case "show" | "display":
            # Enumerate function generate indexing for a list
            for index, item in enumerate(todos):
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
    
