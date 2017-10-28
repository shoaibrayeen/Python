def reverse(str1):
    '''
    Objective: To compute reverse of a string str1
    Input Parameter: str1 - str
    Return Value: str
    '''
    if str1== '':
        return str1
    else:
        return str1[-1] + reverse(str1[:-1])

def main():
    '''
    Objective: To compute reverse of a string entered by user
    Input Parameter: None
    Return Value: None
    '''
    str1 = input('Enter the string: ')
    result = reverse(str1)
    print('Reverse of string ', str1, ' is ', result)

if __name__=='__main__':
    main()
