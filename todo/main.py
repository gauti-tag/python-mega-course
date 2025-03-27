
todos = []
while True:
    user_action = input("Type add, show or exit: ").strip()
    match user_action:
        case "add": 
            user = input("Enter a todo: ")
            todos.append(user)
        case "show" | "display":
            for item in todos:
                print(f"Todo: {item.title()}")
        case "exit":
            break
        case whatever:
            print('Hey ! you entered an unknown command')
    
print("Bye Bye !")
    
