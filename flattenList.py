def flatten(lst1,lst2 = []):
    '''
    Objective: To flatten a list lst1
    Input Parameters: lst1, lst2 - list
    Return Value: lst2- a list
    '''
    for element in lst1:
        if type(element)!= list:
            lst2.append(element)
        else:
            flatten(element, lst2)
    return lst2

def main():
    '''
    Objective: To flatten the list entered by user
    Input Parameter: None
    Return Value: None
    '''
    lst1 = eval(input('Enter the list: '))
    result = flatten(lst1)
    print('Flattened List: ', result)

if __name__=='__main__':
    main()
