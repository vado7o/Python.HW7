import view

def operate(file, operation):
    with open(file, 'r+', encoding = 'utf-8') as file:
        string = file.read()

        if operation == 'write':
            new_str = ','.join(list(map(lambda x: x.strip(), view.askForNewNote())))
            file.writelines(f'\n{new_str}')

        elif operation == 'read':
             return string