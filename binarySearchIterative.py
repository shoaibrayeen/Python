def binarySearch(lst, searchValue):
    '''
    Objective: To search for an element in a sorted list using
    binary search
    Input Parameters: lst - sorted list, searchValue - any type
    Return Value: Index of the matched element, if searchValue is
                  found, None otherwise
    Assumption: List is sorted in increasing order
    '''
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = int((low + high)/2)
        if lst[mid] == searchValue:
            return mid
        elif searchValue < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None

def isSorted(lst):
    '''
    Objective: To find whether the list is sorted in ascending order.
    Input Parameter: lst - sorted list
    Return Value: True if list is sorted
                  False otherwise
    '''
    for i in range(1,len(lst)):
        if lst[i] < lst[i-1]:
            return False
    return True

def main():
    '''
    Objective: To search for an element in the sorted list provided
               as an input by the user
    Input Parameter: None
    Return Value: None
    '''
    lst = eval(input('Enter a sorted list (ascending order): '))
    if not(isSorted(lst)):
        print('Given list is not sorted')
    else:
        searchVal = eval(input('Enter the value to be searched: '))
        print(searchVal, 'found at index', binarySearch(lst, searchVal))

if __name__=='__main__':
    main()
