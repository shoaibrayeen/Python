def printTable(num, nMultiples = 10):
    '''
    Objective: To print multiplication table of a number
    comprising of first nMultiples
    Input Parameters:
        nMultiples: numeric - number of multiples of a number
        to be printed
        num: numeric – number whose multiplication table is to
        be printed
    Output: Multiplication tables of a number
    Return Value: None
    '''
    for multiple in range(1, nMultiples + 1):
        product = num * multiple
        print(num, '*', '%2d' % multiple, '=', '%5d'% product)


def main():
    '''
    Objective: To print multiplication table of a number
    Input Parameter: None
    Return Value: None
    '''
    num = int(input('Enter the number: '))
    printTable(num)

if __name__=='__main__':
    main()
