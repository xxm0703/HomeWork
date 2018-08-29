calc = {}
l = [1, 2, 5, 10, 20, 50]


def change(amount, coins):
    if coins == 0:
        if amount == 0:
            return 1
        return 0

    n = s = 0

    while amount - n * l[coins - 1] >= 0:
        if ((amount - n * l[coins - 1]), coins - 1) in calc.keys():
            s += calc[((amount - n * l[coins - 1]), coins - 1)]
        else:
            s += change(amount - n * l[coins - 1], coins - 1)
        n += 1
    calc[(amount, coins)] = s
    return s


print(change(5, 6))
