def fun(str):
    '''
    objective : reverse of a sentence
    input parameter :
        str : string that contains the sentence
    return value : string that contains reverse of string
    '''
    #approach : converting string to list then reverse of list
    #and then converting list to string
    list=str.split()
    i=0
    j=len(list)-1
    while i < len(list)/2:
        list[i],list[j]=list[j],list[i]
        i=i+1
        j=j-1
    str=' '.join(list)
    return str


str="this"

str2="this is computer science department"

print(fun(str))
print(fun(str2))
