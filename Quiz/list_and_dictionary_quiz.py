list=[1,2,3,4,5,6,7,8,9]

print(list[int(int('4'*2)//7)]) # '4'*2 =='44' and converting it to integer and dividing it by 7

print(list)

list=[4,5,6]  #updating content of list

print(list)

list[:]=[7,8,9] #updating content of list ([:] = start from 0 till end )

print(list)



list1=['a','b','c','d']
list2=['b','a','d','c']

print(list1==list2) #false because list1 and list2 contain same elements but at different positions


dic1={'1':'a','2':'b','3':'c','4':'d'}
dic2={'2':'b','1':'a','4':'d','3':'c'}

print(dic1==dic2) #true
#Dictionaries contain same elements

