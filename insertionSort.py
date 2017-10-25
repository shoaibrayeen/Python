def insertionSort(lst):
    '''
    Objective: To sort the list lst in ascending order using
    insertion sort
    Input Parameter: lst - list
    Return Value: None
    '''
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > temp: # shift lst[j] right
            lst[j + 1] = lst[j]
            j = j-1
        lst[j + 1] = temp

def main():
    '''
    Objective: To sort the list provided as an input by the user
    Input Parameter: None
    Return Value: None
    '''
    lst = eval(input('Enter a list: '))
    print('Sorted List')
    insertionSort(lst)
    print(lst)

if __name__=='__main__':
    main()
