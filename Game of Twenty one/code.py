def init(list):
    for i in range(1,45):
        if i < 12:
            if i == 1:
                list.append(('Spade','Ace'))
            elif i > 1 and i <= 10 :
                list.append(('Spade',i))
            else:
                list.append(('Spade','Jack'))
                list.append(('Spade','Queen'))
                list.append(('Spade','King'))
        elif (i-11) < 12:
            if (i-11) == 1:
                list.append(('Club','Ace'))
            elif (i-11)  > 1 and (i-11) <= 10 :
                list.append(('Club',i-11))
            else:
                list.append(('Club','Jack'))
                list.append(('Club','Queen'))
                list.append(('Club','King'))
        elif (i-22)  < 12:
            if (i-22)  == 1:
                list.append(('Heart','Ace'))
            elif (i-22)  > 1 and (i-22)  <= 10 :
                list.append(('Heart',i-22))
            else:
                list.append(('Heart','Jack'))
                list.append(('Heart','Queen'))
                list.append(('Heart','King'))
        else:
            if (i-33)  == 1:
                list.append(('Diamond','Ace'))
            elif (i-33) > 1 and (i-33) <= 10 :
                list.append(('Diamond',i-33))
            else:
                list.append(('Diamond','Jack'))
                list.append(('Diamond','Queen'))
                list.append(('Diamond','King'))

def shuffle(list):
    import random
    for i in range(51):
        index = random.randint(i,51)
        temp  = list[i]
        list[i] = list[index]
        list[index] = temp


def printname(list , index):
    print(list[index][1] , "of" , list[index][0] , "\n")

def point(list , index):
    if list[index][1]=='Jack' or list[index][1]=='Queen' or list[index][1]=='King':
        return 10
    elif list[index][1] == 'Ace':
        return 11
    else:
        return list[index][1]

def Turn(list , top , sum ):
    if list[top][1] == 'Ace':
        if sum <= 10:
            return 11
        else:
            return 1
    else:
        if list[top][1] == 'Jack' or list[top][1] =='Queen' or list[top][1]=='King':
            return 10
        else:
            return list[top][1]
def probability(list , top , sum):
    count = 0
    if sum <= 10:
        return 1
    for i in range(top , 52):
        if point(list , i ) <= (21 - sum):
            count += 1
    return (count/(51-top))
            
def TwentyOne():
    newGame = 'YES'
    while newGame == 'yes'.upper():
        reply = 'HIT' 
        list=[]
        sumUser = 0
        sumComputer = 0
        init(list)
        shuffle(list)
        top = 0
        print("\n---------------User's Turn---------------\n")
        printname(list , top)
        sumUser += point( list , top)
        top += 1
        printname(list , top)
        sumUser += point( list , top)
        top += 1
        while ( reply == 'Hit'.upper() and sumUser < 21):
            print("\nYour Score\t:\t" , sumUser)

            print("\nThe Probability of getting 21\t:\t%.4f" % probability(list , top , sumUser ))
            reply = input('\nHit or Stay\t:\t')
            reply = reply.upper()
            
            if reply == 'Stay'.upper():
                break
            else:
                temp = Turn(list , top ,sumUser)
                printname(list , top)
                if (sumUser + temp) > 21:
                    print("\nEnd of User's Turn because Score can't be more than 21\n")
                    break
                sumUser += temp
                top += 1
        print("\nYour Score\t:\t" , sumUser)
        print("\n---------------Computer's Turn---------------\n")
        printname(list , top)
        sumComputer += point( list , top)
        top += 1
        printname(list , top)
        sumComputer += point( list , top)
        top += 1
        reply = 'HIT'
        while ( reply == 'Hit'.upper() and sumComputer < 21 ):
            print("\nComputer Score\t:\t",sumComputer)
            if probability(list , top , sumComputer ) > 0.3:
                reply = 'HIT'
            else:
                break
            
            if reply == 'Stay'.upper():
                break
            else:
                temp = Turn(list , top ,sumComputer)
                printname(list , top)
                if ( sumComputer + temp ) > 21:
                    print("\nEnd of Computer's Turn because Score can't be more than 21\n")
                    break
                sumComputer += temp
                top += 1

        print("\nYour Score\t:\t" , sumUser)
        print("\nComputer Score\t:\t",sumComputer)
        if sumUser == 21 or sumUser >= sumComputer:
            print("\nYou won\n")
        else:
            print("\nYou lose\n")
        newGame = input('\nWant to Play new Game\t:\t')
        newGame = newGame.upper()

TwentyOne()
