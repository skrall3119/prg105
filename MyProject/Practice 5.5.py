import random


def start_quiz():
    print("Solve the given equation")
    int1 = get_random_number()
    int2 = get_random_number()
    answer = solve(int1, int2)
    print_equation(int1, int2)
    user_answer = get_user_answer()
    while user_answer != answer:
        print("Please try again")
        user_answer = get_user_answer()
    print("Correct!")


def solve(int1, int2):
    answer = int1 + int2
    return answer


def print_equation(int1, int2):
    print('\n ' + format(int1, ''))
    print('+' + format(int2, '', ))


def get_user_answer():
    user_answer = int(input("\nEnter your answer to the equation "))
    return user_answer


def get_random_number():
    return random.randint(0, 1001)

for count in range(1, 16):
    print("Question #", count)
    start_quiz()
