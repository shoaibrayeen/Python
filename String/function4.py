def fun(string):
    print("Join Operation")
    print("converts tuple into string\t:\t","---".join(("a","b","c","d")))
    print("converts list into string\t:\t","---".join(["a","b","c","d"]))

    print("\nLength of the string\t\t:\t",len(string))

    print("\nusing ljust() function\t\t:\t",string.ljust(30,"*"))
    #About ljust()
    """
    if len(string)<1st arguments , then given character appends to string at
    end until
        len(string)=1st argument
    """
    print("\nusing rjust() function\t\t:\t",string.rjust(30,"*"))
    #About rjust()
    """
    if len(string)<1st arguments , then given character appends to string at
    begining until
        len(string)=1st argument
    """

    print("\nString in Lower case\t\t:\t",string.lower())
    print("\nString in Upper case\t\t:\t",string.upper())

    print("\nstrip string from beginning\t:\t",string.lstrip("tis"))
    print("\nstrip string from end\t\t:\t",string.rstrip("cne."))
    print("\nstrip string from both side\t:\t",string.strip("thcne."))


    print("\nMax character in the string\t:\t",max(string))
    print("\nMin character in the string\t:\t",min(string))
    print("\nMin character in the string\t:\t",min("Computer")) 
string="this is computer science."
fun(string)
