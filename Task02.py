sample_input = [4, 2, 5]
final_input = [2, 5, 4]
marcin_input = [9, 4, 3]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def all_possible_paths(input_data):
    x, y = input_data[0], input_data[1]
    n_moves = input_data[2]
    final_list = [[(x, y)]]

    for i in range(n_moves):
        final_list = singular_move(final_list)
    return final_list


def singular_move(list_of_paths):
    final_list = list()
    for path in list_of_paths:
        for direction in directions:
            appender = path.copy()
            appender.append((path[-1][0] + direction[0], path[-1][1] + direction[1]))
            final_list.append(appender)

    return final_list


def final_probability(list_of_paths):
    probability = 0
    for path in list_of_paths:
        to_add = 0
        for pair in path:
            if (1, 1) > pair or pair > (10, 10):
                to_add = 1
        probability += to_add

    return round(probability / len(list_of_paths), 7)


def final_answer(data_input):
    print()
    print(f"Final answer for an input {data_input} is:")
    print(final_probability(all_possible_paths(data_input)))


final_answer(final_input)
