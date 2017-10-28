def fibonacci(n):
    '''
    Objective: To determine nth term in Fibonacci sequence
    Input Parameter: n- numeric value
    Return Value: result - numeric value
    '''
    assert n > 0
    secondLast = 0
    last = 1
    if n == 1:
        return secondLast
    elif n == 2:
        return last
    for i in range(3, n+1):
        result = secondLast + last
        secondLast = last
        last = result
    return result

def main():
    '''
    Objective: To determine nth term in Fibonacci sequence based
    on user input
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the value of n: '))
    result = fibonacci(n)
    print(n, 'th Fibonacci term', 'is', result)

if __name__=='__main__':
    main()
