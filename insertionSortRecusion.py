def insertInList(list,element,pos=0):
     '''
     objective : To insert a number in sorted list
     Input parameters :
           list : sorted list ( increasing order)
           element : the number which you want to insert
           position : position at which element will be inserted
        return value : list after inserting the number
    '''
    #approach  : using recursion
     
     if(element<list[pos]):
        list.insert(pos,element)
        return list
     elif pos==len(list)-1:
        list.append(element)
        return list
     else:
        pos+=1
        return insertInList(list,element,pos)

def insertionSort(list,count = 0):
     '''
     objective : to sort a list using Insertion Sort Algorithm
     Input parameters :
           list : unsorted list
           count: count till length of list 
        return value : sorted List
    '''
    #approach  : using recursion
     if list==[]:
        return []
     else:
        if (len(list)==count+1):
            return list
        else:
            temp=list[count]
            del list[count]
            insertInList(list,temp,count)
            return insertionSort(list,count+1) 
    

list = [-3,23,-9,12,2,6,1,5,20,12]
print("Unsorted List : ",list)
print("Sorted List : ",insertionSort(list))
