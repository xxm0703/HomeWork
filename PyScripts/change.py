calc = {}
l = [1, 2, 5, 10, 20, 50]


def change(amount, coins):
    if (amount, coins) in calc.keys():
	return calc[(amount, coins)]
    if coins == 0:
    	return 0
    if amount == 0:
    	return 1

    n = s = 0

    while amount - n * l[coins - 1] >= 0:
	s += change(amount - n * l[coins - 1], coins - 1)
        n += 1
    calc[(amount, coins)] = s
    return s


print(change(10000, 6))
