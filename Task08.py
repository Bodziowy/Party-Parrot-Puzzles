sample_input = (3, 4)
final_input = (15, 90)


def final_answer(mxn):
    # The question can be rephrased as "Is there a closed Knight's Tour for given board mxn?"
    # Answer for it, with proper proof, can be found on the Internet.
    # E.g. at  http://gaebler.us/share/Knight_tour.html
    (m, n) = sorted(list(mxn))
    if m < 3 or m == 4:
        return False
    elif m == 3 and n < 10:
        return False
    return not bool(m * n % 2)


print(final_answer(final_input))
