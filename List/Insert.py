def SortList(l,n):
'''
objective        : To insert an element in its proper position into a sorted list.
Input parameters :
               l : Sorted List
               n : element to be inserted
output           : sorted list
'''
if l==[]:
 return l.insert(0,n)
if l[0]>n:
 return l.insert(0,n)
else
 SortList(l[1:],n)
 
