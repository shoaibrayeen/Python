def List(list,element,pos = 0):
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
        return List(list,element,pos)         
   
def main():
    '''
     objective : To insert a number at correct order in sorted list
     approach : using List()
        return value : list after inserting the number
    '''
    list=[int(x) for x in input("Enter the sorted list in increasing order :  " ).split()]
    element=int(input("Enter the element which you want to insert : " ))
    print("List after inserting element : " , List(list ,element) )
if __name__=='__main__':
    main()
