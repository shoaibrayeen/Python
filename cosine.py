def cosine(x):
    '''
    objective: To calculate cosine value of a number.
    input parameter:
          X = value for which cosine value is to be calculated
    return: Cosine value of the number
    '''
    #approach: By  using arithmetic operations to calculate cosine value of a number

    total = 0
    term = 1
    mulBy = -x**2
    epsilon = 0.0001
    nextInSeq = 1
    while(abs(term) > epsilon):
        total += term
        divBy = nextInSeq*(nextInSeq + 1)
        term = term*mulBy/divBy
        nextInSeq+=2
    return total


def main():
    '''
    objective: To input the value from the user for which the cosine value is to be calculated
    input parameter:
          X = value for which cosine value is to be calculated
    '''

    #approach: Get input from the user and calculate value using cosine function

    x = float(input("Enter value to calculate cosine: "))
    print("Cosine of ",x," is",cosine(x))

if __name__=='__main__':
    main()
