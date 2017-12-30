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

def selectionSort(list , count = 0 ):
    '''
    Objective: to sort a list using selection sort algorithm
    Input Parameters:
        list: list to be given
        count: for counting till length of list
    Return Value: sorted List
    '''
    #Approach : using function minIndex()
    if list==[]:
        return []
    elif count==len(list)-1:
            return list
    else:
        temp=minIndex(list,count,len(list)-1)
        list[count],list[temp]=list[temp],list[count]
        return selectionSort(list,count+1)
    

list = [-3,23,-9,12,2,6,1,5]
print("Unsorted List : ",list)
print("Sorted List : ",selectionSort(list))
