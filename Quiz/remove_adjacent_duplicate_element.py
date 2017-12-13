#Remove Adjacent duplicate elements with the element

def count(list ,start,index=0):
    if start+1==len(list):
        return index
    if list[start]==list[start+1]:
        return count(list ,start+1,index+1)
    return index


def fun(list,start=0):
    if list==[]:
        return list
    elif start==len(list):
        return list
    else:
        temp=count(list,start)
        if temp!=0:
            del list[start:start+temp+1]
            return fun(list,start)
        return fun(list,start+1)



list=[1,1,2,2,2,2,2,2,2,3,3,4,4,6,6,6,6,7,5,5,5,5,8,9,10,5,1,2,3,4,7]
print(fun(list))

#output [7, 8, 9, 10, 5, 1, 2, 3, 4, 7]
