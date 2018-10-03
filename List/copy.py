def copy(lst_1, lst_2 = []):
    '''
    Objective: To create copy of a list lst1
    Input Parameters: lst1, lst2 - list
    Return Value: lst2 - list
    '''
    if lst_1==[]:
        return lst_2
    else:
        lst_2.append(lst_1[0])
        copy(lst_1[1:], lst_2)
    return lst_2

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
