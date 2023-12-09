FILEPATH = 'todos.txt'
def print_row():
    """Prints out a list of to-dos"""
    td = get_todos()
#    new_todos = []
#    for item in todos:
#       new_item = item.strip('\n')
#        new_todos.append(new_item)
#    new_todos = [item.strip('\n') for item in todos] this is called 'list comprehension'
    if len(td) > 0:
        for ii, item in enumerate(td):
            item = item.strip('\n')
            print(f"{ii+1}. {item}")
    else:
        print("There are no to dos in the list.")
    pass


def get_todos(filepath=FILEPATH):
    """Gets to-dos from a file, and returns them in a list object"""
    with open(filepath, 'r') as f:
        t = f.readlines()
    return t


def write_todos(todos_arg, filepath=FILEPATH):
    """Takes to-dos from a list object and writes them to a file"""
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)
