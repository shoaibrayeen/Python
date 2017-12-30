def linearSearch(lst, searchValue):
    '''
    Objective: To search for an element in a list using linear
    search
    Input Parameters:
        lst – list
        searchValue - any type
    Return Value: index - numeric value, if searchValue is found,
                  None otherwise
    '''
    for i in range(0, len(lst)):
        if lst[i] == searchValue:
            return i
    return None
def main():
    '''
    Objective: To search for an element in the list provided as an
    input by the user
    Input Parameter: None
    Return Value: None
    '''
    lst = eval(input('Enter a list: '))
    searchVal = eval(input('Enter the value to be searched: '))
    searchResult = linearSearch(lst, searchVal)
    print(searchVal, ' found at index ', searchResult)
    
if __name__=='__main__':
    main()
