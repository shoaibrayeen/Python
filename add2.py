def increment(number):
    '''
    objective: To increment a number
    input: number
    output: The number incremented by 1
    '''
    return number+1

def add2(num1,num2):
    '''
    objective : To add two numbers without using operators or loops
    input: num1 and num2
    output: The sum of num1 and num 2
    '''
    assert num1>=0 and num2>=0
    if num2==0:
        return num1
    else:
        
        num1=increment(num1)
        num2=num2 - 1
        return add2(num1,num2)
    
        
