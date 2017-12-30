def mergeTwoSortedLists(list1,list2,list3=[],index1=0,index2=0) :
    '''
    Objective : To merge two sorted lists into a 3rd list in sorted order
    Input Parametrs :
        list1 : First sorted list
        list2 : Second sorted list
        list3 : Merge sorted list of list1 and list2
        index1 : Using for indexing of list1
        index2 : Using for indexing of list2
    Return Values : Merge Sorted list
    '''
    # Approach : Merge two sorted lists into a 3rd list using recursion
    
    if ( index1 == len(list1) and index2 == len(list2) ) :
        return list3
    elif ( index1 == len(list1) or index2 == len(list2)) :
        if ( index1 == len(list1)) :
            list3.extend(list2[index2:])
            return mergeTwoSortedLists(list1,list2,list3,index1,len(list2))
        else :
            list3.extend(list1[index1:])
            return mergeTwoSortedLists(list1,list2,list3,len(list1),index2)
    elif ( list1[index1] < list2[index2] ) :
        list3.append(list1[index1])
        return mergeTwoSortedLists(list1,list2,list3,index1+1,index2)
    else :
        list3.append(list2[index2])
        return mergeTwoSortedLists(list1,list2,list3,index1,index2+1)


list1=[1,3,5,7]
list2=[1,2,3,4,6,8]
list3=mergeSortedLists(list1,list2)
print('1st Sorted List\t:\t', list1)
print('2nd Sorted List\t:\t', list2)
print('Merge Sorted List:\t', list3)
