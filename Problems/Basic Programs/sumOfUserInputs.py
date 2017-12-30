def main():
    '''
    Objective: To compute sum of numbers entered by user until
    user provides with null string as the input
    Input Parameter: None
    Return Value: None
    '''
    total = 0
    number = input('Enter a number: ')
    while number != '':
        total += int(number)
        number = input('Enter a number: ')
    print('Sum of all input numbers is', total)

if __name__=='__main__':
    main()
