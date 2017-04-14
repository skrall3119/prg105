import pickle


def add(dic):           # adds a new entry to the dictionary
    name = input('Enter the name you wish to add: ')
    email = input('Enter the email you wish to associate with this name: ')
    dic[name] = email
    print(dictionary)


def remove(dic):        # removes the entry of the dictionary
    name = input('Enter the name of the person you want removed from your emails: ')
    del dic[name]
    print(dictionary)


def change(dic):       # allows the user to change the name or email when specified. 
    option = input('Do you want to change the name or the email?: ').lower()
    if option == 'name':
        name = input('Enter the name you want to change: ')
        if name not in dic:
            name = input("That name is not in the list, please enter a name in the list. or use the 'add' command to add a \
            new email address\n")
            while name not in dic:
                name = input('Enter the name you want to change: ')
        new_name = input('Enter the new name: ')
        dic[new_name] = dic[name]
        del dic[name]
        print('\n')
        print(dic)
    elif option == 'email':
        name = input('Enter the name of the persons email you want to change: ')
        if name not in dic:
            name = input('That name is not in the list, please enter a name in the list, or use the add command to add \
            a new name and email combo.: ')
        new_email = input('Enter the new email address: ')
        dic[name] = new_email
        print('\n')
        print(dic)


def show_dic(dic):      # prints the dictionary
    print(dic)

# beginning of main code. opens the file if it exists or creates a new one otherwise.
try:
    dictionary = pickle.load(open('save.p', 'rb'))
except EOFError:
    dictionary = {}

print(dictionary)
commands = 'List of commands: ' + '\n' + 'add' + '\n' + 'remove' + '\n' 'print' + '\n' + 'quit' + '\n' + 'save' + '\n'
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
    elif user == 'save':
        pickle.dump(dictionary, open('save.p', 'wb'))
        print('Progress saved!')
        user = input('Enter a command: ')
    else:
        print('Invalid command.' + '\n' + commands)
        user = input('Enter a command:')
else:
    pickle.dump(dictionary, open('save.p', 'wb'))
