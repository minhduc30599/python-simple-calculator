import os

from art import logo

flag = False

def clear():
    os.system('clear')

def calculate_number(first_num, second_num, oper):
    if oper == '+':
        result = first_num + second_num
    elif oper == '-':
        result = first_num - second_num
    elif oper == '*':
        result = first_num * second_num
    elif oper == '/':
        result = first_num / second_num
    else:
        print("You choose wrong operator")
        clear()

    return result

def continue_or_not(result):
    global flag
    while True:
        y_or_n = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if y_or_n == 'n':
            clear()
            first_result = 0
            flag = True
            break
        elif y_or_n == 'y':
            flag = False
            break

print(logo)

# ask user numbers and operator for calculating
first_number = float(input('What\'s the first number? '))
print('+\n-\n*\n/\n')
operator = input('Pick an operation ')
second_number = float(input('What\'s the next number? '))

first_result = calculate_number(first_number, second_number, operator)

# print first answer
print(f'{first_number} {operator} {second_number} = {first_result}')

# keep calculating or not
continue_or_not(first_result)

# calculating second answer and ask user keep calculating or not
while not flag:
    operator = input('Pick an operation ')
    next_number = float(input('What\'s the next number? '))

    new_result = calculate_number(first_result, next_number, operator)

    print(f'{first_result} {operator} {next_number} = {new_result}')

    continue_or_not(new_result)
    
    first_result = new_result