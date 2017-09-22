def minIndex(list,minI=0,Index=1):
    '''
    Objective: to find the index of the minimum numbrer of the list
    Input Parameters:
        list: list to be given
        upperBound: upper bound of the list
        lowerBound: lower bound of the list
    Return Value: the index of the minimum numbrer of the list
    '''

    #Approach: using recursion
    if Index==len(list):
        return minI
    elif list[Index] > list[minI]:
        return minIndex(list,minI,Index+1)
    else:
        return minIndex(list,Index,Index+1)


    
list = [6,1,5,-76,2,9,8,-9,10,-27]

print("Minimum in the list",minIndex(list))

