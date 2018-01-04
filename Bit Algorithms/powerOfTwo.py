def powerOfTwo(x):
    if ( x & ( x - 1 )) == 0 :
        print( x, "is power of 2.")
    else:
        print( x, "is not power of 2.")

powerOfTwo(14)
powerOfTwo(8)
powerOfTwo(2)
powerOfTwo(1)
powerOfTwo(9)
