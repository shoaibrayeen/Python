# d can be any digit from 1 to 9.
# d + dd + ddd + ... n times
# sum returns the result 

def fun1( d , n ):
    sum=0
    temp=str(d)   #converting d to string and storing it in temp
    for i in range(1,n+1):    #loop start from 1 AND end at n
        sum += int(temp*i)    #multily string by i times and convert it to integer and then add it.
        
    print("\nTotal\t:\t",sum) 



def fun2( d , n ):
    sum=0
    temp=d      #storing d to temp
    for i in range(n):
        sum += temp       #adding temp value to sum
        temp *= 10        
        temp += d         # updating temp to next value so than can use it in next iteration
        
    print("\nTotal\t:\t",sum)


fun1(9,4)
fun2(9,3)
