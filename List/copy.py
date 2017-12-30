def copy(lst1, lst2 = []):
    '''
    Objective: To create copy of a list lst1
    Input Parameters: lst1, lst2 - list
    Return Value: lst2 - list
    '''
    if lst1==[]:
        return lst2
    else:
        lst2.append(lst1[0])
        copy(lst1[1:], lst2)
    return lst2

def main():
    '''
    Objective: To create copy of the list entered by user
    Input Parameter: None
    Return Value: None
    '''
    lst1 = eval(input('Enter the list: '))
    lst2 = copy(lst1)
    print('Copy of list lst1 is ', lst2)

if __name__=='__main__':
    main()
