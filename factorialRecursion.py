def factorial(n):
    '''
    Objective: To compute factorial of a positive number
    Input Parameter: n - numeric value
    Return Value: factorial of n - numeric value
    '''
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    '''
    Objective: To compute factorial of a number provided
    by user
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the number: '))
    result = factorial(n)
    print('Factorial of', n, 'is', result)

if __name__=='__main__':
    main()
