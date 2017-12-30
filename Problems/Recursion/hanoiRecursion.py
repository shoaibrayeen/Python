def hanoi(n, source, spare, target):
    '''
    Objective: To solve problem of Tower of Hanoi using n
    discs and 3 poles
    Input parameters: n, source, spare, target : numeric values
    Return Value: None
    '''
    if n==1:
        print('Move a disk from', source, 'to', target)
    elif n == 0:
        return
    else:
        hanoi(n-1, source, target, spare)
        print('Move a disk from', source, 'to', target)
        hanoi(n-1, spare, source, target)

def main():
    '''
    Objective: To solve Tower of Hanoi problem based on user input
    Input Parameter: None
    Return Value: None
    '''
    n = int(input('Enter the number of discs: '))
    source = int(input('Enter source pole: '))
    spare = int(input('Enter spare pole: '))
    target = int(input('Enter target pole: '))
    hanoi(n, source, spare, target)

if __name__=='__main__':
    main()
