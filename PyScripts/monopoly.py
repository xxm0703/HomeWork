def monop(finish_order=6,games_order=3):

    finish = 10**finish_order
    games = 10**games_order

    import random
    from random import shuffle

    squares = [0 for _ in range(40)]

    dice_values = [1,2,3,4,5,6]

    lenght = len(dice_values)

    games_finished = 0

    while games_finished < games:

        doubles = 0

        position = 0

        turns = 0

        while turns < finish:

            diceroll = [dice_values[int(lenght*random.random())] for _ in range(2)]

            if diceroll[0] == diceroll[1]:
                doubles += 1
            else:
                doubles = 0
            if doubles >= 3:
                position = 10
            else:

                position += sum(diceroll)
                position %= 40

                if position == 30:
                   position = 10


            squares[position] += 1
            turns += 1

        games_finished += 1

    pos_sum = float(sum(squares))

    return [(cell/pos_sum)*100 for cell in squares]


ch = monop(3,3)
ch1 = monop(3,3)

for i in range(len(ch)):
    print("%2d. %.2f\t%.2f" %(i, ch[i], ch1[i]))
