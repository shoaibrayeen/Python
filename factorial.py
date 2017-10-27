def factorial(n):
    '''
    Objective: To compute factorial of a number
    Input Parameter: n - numeric value
    Return Value: fact - numeric value
    '''
    fact = 1
    assert n >= 0
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def main():
    '''
    Objective: To compute factorial of a number provided
    by user
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the number: '))
    fact = factorial(n)
    print('Factorial of', n, 'is', fact)
    
if __name__=='__main__':
    main()
