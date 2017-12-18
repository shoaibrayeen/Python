def fun(string):
    print("using capitalize()\t\t:\t",string.capitalize())
    print("using center()\t\t\t:\t",string.center(30,'z'))
    #About Center
    #1st argument must be greater than length of string in center()
    #2nd argument must be a single character in center()
    #if 1st argument < len(string) , return the string

    print("using count(string)\t\t:\t" ,string.count("this"))
    print("using count(string,beg)\t\t:\t" ,string.count("this",2))
    print("using count(string , beg ,end)\t:\t" ,string.count("this",1,12)) 
    ## About Count
    """
    1. if we pass one argument in count(),
        then it checks from 0 till length of string
    2. if we pass two argument in count(),
        then it checks from the 2nd argument till length of string
    3. if we pass three argument in count(),
        then it checks from 2nd argument till 3rd arguments
    """
    #return the count

    print("Encoding and Decoding done by 'UTF-16")
    string=string.encode('UTF-16',"error")
    print("Encoded String\t\t\t:\t",string)
    string=string.decode('UTF-16',"error")
    print("Decoded String\t\t\t:\t",string)

    

string="this is computer science"
fun(string)
