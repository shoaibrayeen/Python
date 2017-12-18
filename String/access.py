def fun(string):
    print("string[0]\t:\t", string[0])
    print("string[:]\t:\t",string[:])
    print("string[2:10]\t:\t",string[2:10])
    print("Updated String\t:\t" , string[:4]+" is updated string")
    print("* Operator\t:\t",string*2)
    print(" using 'in'\t:\t", 'T' in string)
    print(" using 'not in'\t:\t", 'T' not in string)
    

    

string="this is computer science"
fun(string)
