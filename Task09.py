sample_input = [50.3, 0.7, 42.1]
final_input = [83.83, 0.29, 72.46]


def force_in_newtons(data):
    # F = m*a = 120000*[(v0 - v)/t + a0]
    force = 120000.0
    force *= ((data[0] - data[1]) / data[2] + 3.7)

    return round(force, 2)


print(force_in_newtons(final_input))
