from itertools import chain, combinations

sample_input = [
    [7],
    [1, 1],
    [2, 6],
    [3, 10],
    [5, 16]]

final_input = [
    [387],
    [49, 24],
    [29, 17],
    [17, 18],
    [55, 60],
    [74, 10],
    [61, 95],
    [77, 15],
    [62, 96],
    [68, 91],
    [43, 20]]


def final_answer(input_data):
    max_weight = input_data[0][0]
    proper_data = input_data[1:]
    final_weight = 0
    final_value = 0
    final_subset = list()

    for subset in powerset(proper_data):
        temporary_weight = 0
        temporary_value = 0
        for pair in subset:
            temporary_weight += pair[0]
            temporary_value += pair[1]
        if temporary_weight <= max_weight and temporary_value > final_value:
            final_weight, final_value = temporary_weight, temporary_value
            final_subset = subset

    print(f"\nWaga maksymalna: {max_weight}")
    print(f"Waga koncowa: {final_weight}, wartosc koncowa: {final_value}")
    print(final_subset)


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1))


final_answer(final_input)
