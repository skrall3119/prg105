import pickle


def add(dic):
    name = input('Enter the name you wish to add: ')
    email = input('Enter the email you wish to associate with this name: ')
    dic[name] = email
    print(dictionary)


def remove(dic):
    name = input('Enter the name of the person you want removed from your emails: ')
    del dic[name]
    print(dictionary)


def change(dic):
    option = input('Do you want to change the name or the email?: ').lower()
    if option == 'name':
        name = input('Enter the name you want to change: ')
        if name not in dic:
            name = input("That name is not in the list, please enter a name in the list. or use the 'add' command to add a \
            new email address:")
        new_name = input('Enter the new name: ')
        dic[new_name] = dic[name]
        del dic[name]
        print('\n' + dic)


def show_dic(dic):
    print(dic)

dictionary = {}
print(dictionary)
commands = 'List of commands: ' + '\n' + 'add' + '\n' + 'remove' + '\n' 'print' + '\n' + 'quit' + '\n'
print(commands)
user = input("Enter a command: ").lower()
while user != 'quit':
    if user == 'add':
        add(dictionary)
        user = input('Enter a command: ')
    elif user == 'remove':
        remove(dictionary)
        user = input('Enter a command: ')
    elif user == 'change':
        change(dictionary)
        user = input('Enter a command: ')
    elif user == 'print':
        print(dictionary)
        user = input('Enter a command: ')
