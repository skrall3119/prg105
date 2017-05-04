def translate(number):
    if '-' in number:
        num_list = number.split('-')
        new_number = ''
        for count in num_list:
            if num_list[count].isdigit():
                new_number += num_list [count]
            if num_list[count].isalpha():
                for letter in num_list[count]:
                    num_list[count][letter].lower()
                    if num_list[count][letter] in 'abc':
                        new_number += '2'
                    elif num_list[count][letter] in 'def':
                        new_number += '3'
                    elif num_list[count][letter] in 'ghi':
                        new_number += '4'
                    elif num_list[count][letter] in 'jkl':
                        new_number += '5'
                    elif num_list[count][letter] in 'mno':
                        new_number += '6'
                    elif num_list[count][letter] in 'pqrs':
                        new_number += '7'
                    elif num_list[count][letter] in 'tuv':
                        new_number += '8'
                    elif num_list[count][letter] in 'wxyz':
                        new_number += '9'

        print(num_list)
    else:
        pass
def check(value):
    pass

translate('773-202-LUNA')
