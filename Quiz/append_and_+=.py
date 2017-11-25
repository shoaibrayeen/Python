def fun1(list=[1,2,3]):
    #Append 6 in list
    print("\nBefore Appending in List\t:",list)
    list.append(6)
    print("\nAfter Appending in List\t\t:",list)
    return list

def fun2(list=[1,2,3]):
    #Add 7 in list
    print("\n\n\n\n\nBefore Adding in List\t\t:",list)
    list += [7]
    print("\nAfter Adding in List\t\t:",list)
    return list

print("\n\nUsing Append\t\t\t:",fun1())
print("\nUsing += operator\t\t:",fun2())



'''
output :

Before Appending in List	: [1, 2, 3]
After Appending in List		: [1, 2, 3, 6]
Using Append			: [1, 2, 3, 6]

Before Adding in List		: [1, 2, 3]
After Adding in List		: [1, 2, 3, 7]
Using += operator		: [1, 2, 3, 7]

'''
