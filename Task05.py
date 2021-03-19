from math import atan, pi

sample_input = [5, 5, 5, 10, 45, 3]
final_input = [73, 42, 86, 95, 144, 10]


def ship_angle(coordinates):
    angle = atan((coordinates[2] - coordinates[0]) / (coordinates[3] - coordinates[1]))
    return round(angle * 180 / pi)


def final_answer(input_data):
    ship = input_data[:4]
    wind_direction = input_data[4]
    wind_drift = input_data[5]

    print()
    print(f"Statek {ship} płynie pod kątem {ship_angle(ship)} stopni.")
    print(f"Wiatr wieje na niego pod kątem {wind_direction} stopni z siłą {wind_drift}.")

    wind_side = (wind_direction - ship_angle(ship)) % 360
    if wind_side < 180:
        wind_drift *= -1
    elif wind_side == 180 or wind_side == 0:
        wind_drift = 0

    print(f'Po uwzględnieniu wiatru finalną odpowiedzią jest {(ship_angle(ship) + wind_drift) % 360}.')


final_answer(final_input)
