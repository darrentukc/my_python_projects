# inputs
#

input = "-2879+-?5584=-?8463"

factors, result = input.split('=')
operator = ''

# splitting up factors

## if + operator

if '+' in factors:
    x_factor, y_factor = factors.split('+')
    operator = '+'

## if * operator

elif '*' in factors:
    x_factor, y_factor = factors.split('*')
    operator = '*'

## if - operator

elif '-' in factors:
    operator = '-'
    temp_list = factors.split('-')

    negative_index = []

    for index in range(len(temp_list)):
        if temp_list[index] == '':
            negative_index.append(index)

    for index in negative_index[::-1]:
        temp_list[index + 1] = '-' + temp_list[index + 1]
        temp_list.pop(index)

    x_factor = temp_list[0]
    y_factor = temp_list[1]

## create list of existing digits

input_digit_list = []
for item in input:
    try:
        input_digit_list.append(int(item))
    except:
        pass

## create list of non existing digits

unverified_possible_digit_list = []
for num in range(0, 10):
    if num not in input_digit_list:
        unverified_possible_digit_list.append(num)

## test if possible digit list makes invalid number

verified_possible_digit_list = []

for num in unverified_possible_digit_list:
    test_x = int(x_factor.replace('?', str(num)))
    test_y = int(y_factor.replace('?', str(num)))
    # print(len(str(test_x)), len(x_factor), len(str(test_y)), len(y_factor))
    if len(str(test_x)) == len(x_factor) and len(str(test_y)) == len(y_factor):
        if test_x != 0 and test_y != 0:
            verified_possible_digit_list.append(num)

# print(verified_possible_digit_list)
#
## check for correct equation using verified_possible_digit_list

possible_answer_list = []

for digit in verified_possible_digit_list:
    x_factor_replaced = int(x_factor.replace('?', str(digit)))
    y_factor_replaced = int(y_factor.replace('?', str(digit)))
    result_replaced = int(result.replace('?', str(digit)))
    if operator == '+':
        if x_factor_replaced + y_factor_replaced == result_replaced:
            possible_answer_list.append(digit)
    elif operator == '*':
        if x_factor_replaced * y_factor_replaced == result_replaced:
            possible_answer_list.append(digit)
    elif operator == '-':
        if x_factor_replaced - y_factor_replaced == result_replaced:
            possible_answer_list.append(digit)

if len(possible_answer_list) == 0:
    print(-1)
else:
    print(possible_answer_list[0])
