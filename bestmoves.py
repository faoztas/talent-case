checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}

def find_moves(checkers, dice1, dice2):

    ##################################################
    importantDoors = [5, 6, 7, 8, 17, 18, 19, 20]
    score = []
    bestMoves = []
    ##################################################

    for stamp1 in checkers.keys():
        point1 = stamp1 + dice1                             # Taş ve zar ile pozisyon hesabı

        if point1 < 24:                                     # Tavla tahta sınırları kontrolü
            for stamp2 in checkers.keys():
                point2 = stamp2 + dice2                     # Taş ve zar ile pozisyon hesabı

                if point2 < 24:                             # Tavla tahta sınırları kontrolü,
                    copyCheckers = checkers.copy()

                    if point1 in copyCheckers:              # Hareket tanımlama
                        copyCheckers[point1] += 1
                    else:
                        copyCheckers[point1] = 1

                    if point2 in copyCheckers:              # Hareket tanımlama
                        copyCheckers[point2] += 1
                    else:
                        copyCheckers[point2] = 1

                    copyCheckers[stamp1] -= 1               # Hareket tamamlama
                    copyCheckers[stamp2] -= 1

                    beforeScore = 0                         # Puan sıfırlama
                    afterScore = 0

                    for i in checkers.keys():               # Mevcut puan hesaplama
                        if checkers[i] == 1:
                            beforeScore -= 1
                        if checkers[i] == 2:
                            if i in importantDoors:
                                beforeScore += 2
                            else:
                                beforeScore += 1
                        if checkers[i] > 2:
                            score.append(i)

                    for i in copyCheckers.keys():           # Hamle sonrası hesaplama
                        if copyCheckers[i] == 1:
                            afterScore -= 1
                        if copyCheckers[i] == 2 and i not in score:
                            if i in importantDoors:
                                afterScore += 2
                            else:
                                afterScore += 1

                    tempScore = afterScore - beforeScore    # Toplam puanlama

                    if tempScore > 0:
                        bestMoves.append(((stamp1, point1), (stamp2, point2), tempScore))
    return bestMoves

print(find_moves(checkers, 6, 1))