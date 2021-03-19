sample_input = [[1, 5],
                [1, 2, 1],
                [1, 3, 2],
                [1, 4, 3],
                [3, 5, 5],
                [4, 3, 4],
                [4, 5, 1]]

final_input = [[2, 4],
               [1, 6, 8],
               [1, 31, 2],
               [1, 2, 16],
               [31, 33, 2],
               [31, 32, 13],
               [6, 31, 10],
               [6, 5, 1],
               [35, 4, 16],
               [33, 34, 3],
               [5, 4, 16],
               [32, 34, 15],
               [32, 33, 18],
               [32, 35, 9],
               [2, 4, 6],
               [2, 31, 9],
               [34, 35, 16]]

sample_input2 = [[1, 14],
                 [1, 2, 2],
                 [1, 3, 2],
                 [1, 4, 3],
                 [3, 4, 2],
                 [3, 14, 5],
                 [4, 3, 4],
                 [4, 14, 3]]


def one_travel(plan, possible_routes_list: list, current_cost: int = 0, history: str = ""):
    reduced_routes_list = possible_routes_list.copy()
    possible_outcomes = []
    output = []
    if history == "":
        history = str(plan[0])
    for route in possible_routes_list:
        if route[0] == plan[0]:
            reduced_routes_list.remove(route)
            possible_outcomes.append([(route[1], plan[1]), route[2]])
    for plan_and_cost in possible_outcomes:
        output.append(
            [plan_and_cost[0], reduced_routes_list, current_cost + plan_and_cost[1], history+f"→{plan_and_cost[0][0]}"])

    return output


def final_answer(input_data):
    possible_outcomes = one_travel(input_data[0], input_data[1:])
    finished_routes_list = []

    while possible_outcomes:
        last_route = possible_outcomes.pop()
        if last_route:
            if last_route[0][0] == last_route[0][1]:
                finished_routes_list.append((last_route[3], last_route[2]))
            else:
                possible_outcomes.extend(one_travel(*last_route))

    print("\nFrom all the possible routes reaching destination:")
    cheapest_cost = finished_routes_list[0][1]
    for route in finished_routes_list:
        print(route)
        if route[1] < cheapest_cost:
            cheapest_cost = route[1]
    print(f'The cheapest one costs {cheapest_cost}')


final_answer(final_input)
