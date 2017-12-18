def fun(string):
    print("String is AlphaNumeric\t\t:\t",string.isalnum())
    print("String is AlphaNumeric\t\t:\t","mca1styear123".isalnum())
    #about isalnum()
    """
    This method returns true if all the characters in the string are
    alphanumeric and there is at least one character, false otherwise.
    """

    print("String is Alphabetic\t\t:\t",string.isalpha())
    print("String is Alphabetic\t\t:\t","mca1styear123".isalpha())
    print("String is Alphabetic\t\t:\t","mca".isalpha())
    #about isalpha()
    """
    This method returns true if all the characters in the string are
    alphabetic and there is at least one character, false otherwise.
    """

    print("String contains digits only\t:\t",string.isdigit())
    print("String contains digits only\t:\t","123".isdigit())

    print("string contains lowercase\t:\t",string.islower())
    print("string contains lowercase\t:\t","Information".islower())
    print("string contains uppercase\t:\t",string.isupper())
    print("string contains uppercase\t:\t","INFORMATION".isupper())

    print("string is numeric\t\t:\t",string.isnumeric())
    print("string is numeric\t\t:\t","12345".isnumeric())

    print("string contains space\t\t:\t",string.isspace())
    print("string contains space\t\t:\t","       ".isspace())
    #isspace() checks only space

    print("string contains title\t\t:\t",string.istitle())
    print("string contains title\t\t:\t","Information Security".istitle())
    #istitle() checks [^A-Z][a-zA-Z]* type string
string="this is \t computer science."
fun(string)
