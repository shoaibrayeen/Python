def isPalindrome(str1):
    '''
    Objective: To check whether a string str1 is palindrome
    Input Parameter: str1- string
    Return Value: True or False
    '''
    if str1 == '':
        return True
    else:
        return (str1[0]==str1[-1] and isPalindrome(str1[1:-1]))

def main():
    '''
    Objective: To check whether the string entered by user is
               palindrome
    Input Parameter: None
    Return Value: None
    '''
    str1 = input('Enter the string: ')
    if (isPalindrome(str1)):
        print('String is a palindrome')
    else:
        print('String is not a palindrome')

if __name__=='__main__':
    main()
