def mySine(x):
    '''
    Objective: To find sum of sine series until the absolute value
    of newTerm becomes smaller than epsilon
    Input Parameter: x - numeric value in radians
    Return Value: total - numeric value
    '''
    epsilon = 0.00001
    multBy = -x**2
    term = x
    total = x
    nxtInSeq = 2.0
    while abs(term) > epsilon:
        divBy = nxtInSeq*(nxtInSeq+1)
        term = term * multBy / divBy
        total += term
        nxtInSeq += 2
    return total
