checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
important_doors = [5, 6, 7, 8, 17, 18, 19, 20]
neoc = checkers.copy()

def find_moves(checkers, dice1, dice2)
    for stamp1 in checkers.keys():
        point1 = stamp1 + dice1

        for stamp2 in checkers.keys():
            point2 = stamp2 + dice2

        if point1 in neoc:
            neoc[point1] += 1
        else:
            neoc[point1]=1


print(find_moves(checkers, 6, 1))