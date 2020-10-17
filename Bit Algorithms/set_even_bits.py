def evenbitsetnumber(n):
    count = 0
    res = 0
    temp = n 
    while(temp > 0):
        if (count % 2 == 1): 
            res |= (1 << count) 
  
        count+=1
        temp >>= 1
          
    # return OR number 
    return (n | res) 
  
n = input('Enter Number\t:\t');
print(evenbitsetnumber(n))
