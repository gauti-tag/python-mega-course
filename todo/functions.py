def get_todos(filepath = 'todo/todos.txt'):
    """ 
        Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_content_local:
        todos_local = file_content_local.readlines()
    return todos_local


def write_todos(todos_arg, filpath = 'todo/todos.txt'):
    """ write the to-do items list in the text file """
    with open(filpath, 'w') as file_content_local:
        file_content_local.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
