def summation(n):
    '''
    Objective: To find sum of first n positive integers
    Input Parameter: n - numeric value
    Return Value: total - numeric value
    '''
    total = 0
    for count in range(1, n + 1):
        total += count
    return total

def main():
    '''
    Objective: To find sum of first n positive integers based on user
    input
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter number of terms: '))
    total = summation(n)
    print('Sum of first', n, 'positive integers: ', total)
    
if __name__=='__main__':
    main()
