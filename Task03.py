from math import sqrt

input_data = [
    (46.51318, 6.71838),
    (46.57898, 6.62875),
    (46.57997, 6.7173)]

tube_stations = [
    ('A', 46.52476, 6.58532),
    ('B', 46.59845, 6.68645),
    ('C', 46.58868, 6.66512),
    ('D', 46.59018, 6.65745),
    ('E', 46.55992, 6.59179)]


def distance_between_three_points(station_coordinates):
    distance = 0
    for point in input_data:
        distance += distance_between_two_points(station_coordinates, point)
    return distance


def distance_between_two_points(a, b):
    x = (a[0]-b[0])**2
    y = (a[1]-b[1])**2
    distance = sqrt(x + y)
    return distance


def final_answer(list_of_stations):
    answer = ""
    smallest_distance = distance_between_three_points(tuple([list_of_stations[0][1], list_of_stations[0][2]]))
    for station in list_of_stations:
        three_points = distance_between_three_points(tuple([station[1], station[2]]))
        if three_points < smallest_distance:
            smallest_distance = three_points
            answer = station[0]

    print(f"\nStation {answer} is the best!")


final_answer(tube_stations)
