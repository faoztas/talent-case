checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}
importantDoors = [5, 6, 7, 8, 17, 18, 19, 20]
neoCheckers = checkers.copy()
beforeScore = 0
afterScore = 0

def find_moves(checkers, dice1, dice2)
    for stamp1 in checkers.keys():
        point1 = stamp1 + dice1             #Taş ve zar ile pozisyon hesabı

        if point1 < 24:                     #Tavla tahta sınırları kontrolü
            for stamp2 in checkers.keys():
                point2 = stamp2 + dice2     #Taş ve zar ile pozisyon hesabı

                if point2 < 24:             #Tavla tahta sınırları kontrolü

                    if point1 in neoCheckers:
                        neoCheckers[point1] += 1   #kapı alma
                    else:
                        neoCheckers[point1] = 1

                    if point2 in neoCheckers:
                        neoCheckers[point2] += 1   #kapı alma
                    else:
                        neoCheckers[point2] = 1

                    neoCheckers[stamp1] -= 1       #hareket tamamlama
                    neoCheckers[stamp2] -= 1


print(find_moves(checkers, 6, 1))