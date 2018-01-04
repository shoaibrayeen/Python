a=10
b=20
def swapUsingXOR(a,b):
    print("Before Swapping\t:\ta = " , a , " b = " , b )
    a ^=b
    b ^=a
    a ^=b
    print("After Swapping\t:\ta = " , a , " b = " , b )



swapUsingXOR(a,b)
