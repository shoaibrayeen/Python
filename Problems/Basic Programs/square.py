def printSquares():
    '''
    Objective: To print squares of positive numbers entered by
    the user. The program terminates if user enters null string.
    Input Parameter: None
    Return Value: None
    '''
    while True:
        numStrng = input('Enter an integer, to end press Enter: ')
        if numStrng == '':
            break
        number = int(numStrng)
        print(number, '^ 2 =', number ** 2)
    print('End of input!!')
