def fun(string):
    print("endswith(suffix)\t:\t",string.endswith("science."))
    print("endswith(suffix)\t:\t",string.endswith("science.",15))
    print("endswith(suffix)\t:\t",string.endswith("science.",0,len(string)))
    ##About endswith()
    """
    1. one argument -> checks in the whole string
    2. two argument -> checks from 2nd argument
    3. three argument -> checks from 2nd argument till 3rd argument
    """
    #return True if found ,otherwise False

    print("Default expandtabs()\t:\t" , string.expandtabs())
    print("Given expandtabs()\t:\t" , string.expandtabs(6))
    #About expandtabs()
    """
    1. checks "\t" in string , replace with 8 spaces if find
    2. if an integer is passeed , then replace with given number of spaces
        if find
    
    """

    print("find(substring)\t\t:\t",string.find("is"))
    print("find(substring,beg)\t:\t",string.find("is",5))
    print("find(substring,beg,end)\t:\t",string.find("is",4,len(string)))
    print("find(substring)\t\t:\t",string.find("not find"))
    #About find()
    """
    1. one argument -> checks in the whole string
    2. two argument -> checks from 2nd argument
    3. three argument -> checks from 2nd argument till 3rd argument
    """
    #return index if found , otherwise -1

    print("index(substr)\t\t:\t",string.index("is"))
    print("index(substr,beg)\t:\t",string.index("is",5))
    print("index(substr,beg,end)\t:\t",string.index("is",4,len(string)))
    #print("index(substring)\t\t:\t",string.index("not find"))
    #About index()
    """
    1. one argument -> checks in the whole string
    2. two argument -> checks from 2nd argument
    3. three argument -> checks from 2nd argument till 3rd argument
    """
    #return index if found , otherwise raises an exception


    #difference between index() and find()
    # found then return index by both functions
    # not found then index-> raises an exception
    # not found then find -> return -1
    

string="this is \t computer science."
fun(string)
