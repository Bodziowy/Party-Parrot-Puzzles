sample_input = "1 2 + 3 *"
final_input = "91.78 35.20 91.79 - + 29.09 82.39 96.03 - * *"

operator_list = ['+', '-', '*']


def reverse_polish_notation(input_string):
    stos = []
    for elem in input_string.split():
        if elem not in operator_list:
            stos.append(float(elem))
        else:
            stos.append(operator(stos.pop(), stos.pop(), elem))

    return round(stos[0], 4)


def operator(b, a, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b


def final_answer(input_data):
    print()
    print(reverse_polish_notation(input_data))


final_answer(final_input)
