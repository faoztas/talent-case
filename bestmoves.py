checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}

def find_moves(checkers, dice1, dice2):

##################################################
    importantDoors = [5, 6, 7, 8, 17, 18, 19, 20]
    score = []
    bestMoves = []
    copyCheckers = checkers.copy()
    beforeScore = 0
    afterScore = 0
##################################################

    for stamp1 in checkers.keys():
        point1 = stamp1 + dice1             #Taş ve zar ile pozisyon hesabı

        if point1 < 24:                     #Tavla tahta sınırları kontrolü
            for stamp2 in checkers.keys():
                point2 = stamp2 + dice2     #Taş ve zar ile pozisyon hesabı

                if point2 < 24:             #Tavla tahta sınırları kontrolü

                    if point1 in copyCheckers:
                        copyCheckers[point1] += 1   #kapı alma
                    else:
                        copyCheckers[point1] = 1

                    if point2 in copyCheckers:
                        copyCheckers[point2] += 1   #kapı alma
                    else:
                        copyCheckers[point2] = 1

                    copyCheckers[stamp1] -= 1       #hareket tamamlama
                    copyCheckers[stamp2] -= 1

                    for i in checkers.keys():       #mevcut puanı hesaplama
                        if checkers[i] == 1:
                            beforeScore -= 1
                        if checkers[i] == 2:
                            if i in importantDoors:
                                beforeScore += 2
                            else:
                                beforeScore +=1
                        if checkers[i] > 2:
                            score.append(i)

                    for i in copyCheckers.keys():   #hamle sonrası puan hesaplama
                        if copyCheckers[i] == 1:
                            afterScore -= 1
                        if copyCheckers[i] == 2 & i not in score:
                            if i in importantDoors:
                                afterScore += 2
                            else:
                                afterScore += 1


                    if afterScore - beforeScore > 0:
                        bestMoves.append((stamp1,point1),(stamp2,point2),afterScore-beforeScore)
    return bestMoves



print(find_moves(checkers, 6, 1))