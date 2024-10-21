FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    '''returns the existing todos that is already stored in the todos.txt'''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos, filepath=FILEPATH):
    """writes todos in the todos.txt file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__' :
    print("hello World")