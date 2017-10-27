def deepCopy(lst1, lst2 = []):
    '''
    Objective: To create deep copy of a list lst1
    Input Parameters: lst1, lst2 - list
    Return Value: lst2 - list
    '''
    if lst1==[]:
        pass
    else:
        if type(lst1[0]) != list:
            lst2.append(lst1[0])
        else:
            lst2.append([])
            deepCopy(lst1[0], lst2[-1])
        deepCopy(lst1[1:], lst2)
    return lst2

def main():
    '''
    Objective: To create deep copy of list entered by user
    Input Parameter: None
    Return Value: None
    '''
    lst1 = eval(input('Enter the list: '))
    lst2 = deepCopy(lst1)
    print('Deep copy of list lst1 is ', lst2)

if __name__=='__main__':
    main()
