def increment(number):
    '''
     objective: increment a given number by 1
     input parameter:
         number: number which is to be incremented
     return value: incremented number
     '''

    #approach: 1 is added to the number
    
    number = number + 1

    return number



def predecessor(number1,number2=0):
    '''
     objective: predecessor of a number
     input parameter:
         number1: number entered by user
        
     return value: predecessor of a number
     '''
    #approach: by calling predecessor2 function recursively

    if number1 == 0:
        return 0
    elif increment(number2) == number1:
        return number2
    else:
        return predecessor(number1,increment(number2))




def main():
    '''
     objective: predecessor of user entered number
     input values:
         number: first number entered by user
         
     output value: predecessor of user entered number
     '''
    #approach:by calling predecessor1 function

    number = int(input("enter the first number: "))
    print("predecessor of a number: " , predecessor(number))

if (__name__=='__main__'):
    main()
