def printTriangle(ch):
    '''
        objective : to print Triangle
        input parameters : 
            ch : input of symbol 
        approach  : to print some lines of symbol
    '''
    print("         " , ch)    
    print("       " , ch , ch , ch)
    print("      " , ch , ch , ch , ch , ch )
    print("    " , ch , ch , ch , ch , ch , ch  , ch )
    print("  " , ch , ch , ch , ch , ch , ch , ch , ch , ch )
    
def main():    
    '''
        objective : to print Triangle
         user inputs : 
            ch : input of symbol 
        approach  : to use function printTriangle()
    '''
    ch=input("Enter symbol ")
    printTriangle(ch)
    
if __name__ == '__main__':
    main()
print("End of the Program")
