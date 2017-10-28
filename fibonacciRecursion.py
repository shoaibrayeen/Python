def fibo(n):
    '''
    Objective: To determine nth term in Fibonacci sequence
    Input Parameter: n: numeric value
    Return Value: nth Fibonacci term - numeric
    '''
    assert n > 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    '''
    Objective: To determine nth term in Fibonacci sequence
    based on user input
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the value of n: '))
    result = fibo(n)
    print(n, 'th Fibonacci term', 'is', result)

if __name__=='__main__':
    main()
