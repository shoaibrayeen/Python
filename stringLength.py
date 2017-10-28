def length(str1):
    '''
    Objective: To determine length of the input string
    Input Parameter: str1- string
    Return Value: numeric
    '''
    if str1== '':
        return 0
    else:
        return 1+length(str1[1:])

def main():
    '''
    Objective: To determine length of string entered by user
    Input Parameter: None
    Return Value: None
    '''
    str1 = input('Enter the string: ')
    result = length(str1)
    print('Length of string ', str1, ' is ', result)

if __name__=='__main__':
    main()
