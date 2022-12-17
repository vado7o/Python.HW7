import view
import operate_module as wr
import os


def startProgram():
    os.system('cls')

    if view.askForChoice() == 1:
        if view.askForFormat() == '1':
            wr.operate('phonebook.txt', 'write')
        else: wr.operate('phonebook.csv', 'write')
        print('\nИнформация успешно записана в книгу !!!\n')

    else:
        if view.askForFormat() == '1':
            print('\n{}\n'.format(wr.operate('phonebook.txt', 'read')))
        else: print('\n{}\n'.format(wr.operate('phonebook.csv', 'read')))