list2=[1,2,3]
def fun1(list=[]):
    #Append given element to the list
    list.append(list2)    #append [1,2,3] at 1st positin
    list.append('123456') #append '123456' to updated list
    return list

def fun2(list=[]):
    #Divide given element into single element and then append to the list
    list.extend(list2)
    list.extend('123456') #append '1','2','3','4','5','6' to updated list
    return list


print("\nUsing Append\t:",fun1())
print("\nUsing Extend\t:",fun2())


'''
output :
Using Append	: [[1, 2, 3], '123456']

Using Extend	: [1, 2, 3, '1', '2', '3', '4', '5', '6']

'''
