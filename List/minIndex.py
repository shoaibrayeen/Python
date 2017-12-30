def minIndex(list,lowerBound,upperBound):
    '''
    Objective: to find the index of the minimum numbrer of the list
    Input Parameters:
        list: list to be given
        upperBound: upper bound of the list
        lowerBound: lower bound of the list
    Return Value: the index of the minimum numbrer of the list
    '''

    #Approach: using recursion
    if upperBound==lowerBound:
        return upperBound
    elif list[upperBound] > list[lowerBound]:
        return minIndex(list,lowerBound,upperBound-1)
    else:
        return minIndex(list,lowerBound+1,upperBound)

list = [6,1,5,2,9,8,-9,1]

print("Minimum in the list",minIndex(list,0,2))
