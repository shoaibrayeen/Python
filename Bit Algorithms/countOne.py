def countOne (n):
    count=0
    while( n ):
        n = n&(n-1)
        count=count+1
    return count

print("the number of ones in the binary representation of 5 are " , countOne(5))

print("the number of ones in the binary representation of 7 are " , countOne(7))

print("the number of ones in the binary representation of 18 are " , countOne(18))


print("the number of ones in the binary representation of 33 are " , countOne(33))
