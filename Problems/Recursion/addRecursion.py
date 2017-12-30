def increment(number):
    '''
    objective: Increment given number by 1
    inputs:
    number: number entered by user
    return value: Increment Number
    '''
    '''
    approach: add 1 to given number
    '''
    return number + 1

def add(number1,number2):
    '''
    objective: Add two numbers without recursion
    inputs:
           number1: first number 
           number2: second number
    return value: Sum of the numbers
    '''
    '''
    approach: using increment(number) function recursively
    '''
    if number2 == 0:
        return number1
    elif number2 < 0 :
        return add(number1-1, increment(number2))
    else:
        return add(increment(number1), number2 - 1)

def main():
    '''
    objective: Add two numbers without recursion
    inputs:
           number1: first number 
           number2: second number
    return value: Sum of the numbers
    '''
    number1 = int(input( "Enter First Number  : " ))
    number2 = int(input( "Enter Second Number : " ))
    print("Sum of Numbers      :",add(number1,number2))
    print("End of Main")
    
if __name__ == "__main__":
    main()
    print("End of Program")
