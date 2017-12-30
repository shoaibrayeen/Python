def bubbleSort(lst):
    '''
    Objective: To sort the list lst in ascending order using bubble
    sort
    Input Parameter: lst - list
    Return Value: None
    '''
    n = len(lst)-1 # highest valid index in the list
    for i in range(0, n):
        for j in range(n, i, -1):
            if lst[j] < lst[j - 1]: # interchange if out of order
                lst[j], lst[j - 1] = lst[j - 1], lst[j]

def main():
    '''
    Objective: To sort the list provided as an input by the user
    Input Parameter: None
    Return Value: None
    '''
    lst = eval(input('Enter the list: '))
    print('Sorted List')
    bubbleSort(lst)
    print(lst)

if __name__=='__main__':
    main()
