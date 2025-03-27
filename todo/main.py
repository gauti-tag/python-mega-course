
todos = []
while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    match user_action:
        case "add": 
            user = input("Enter a todo: ")
            todos.append(user)
        case "show" | "display":
            for item in todos:
                print(f"Todo: {item.title()}")
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] =  new_todo
        case "exit":
            break
        case whatever:
            print('Hey ! you entered an unknown command')
    
print("Bye Bye !")
    
