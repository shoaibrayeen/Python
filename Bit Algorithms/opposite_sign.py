def oppositeSigns(x, y): 
    return ((x ^ y) < 0); 
  
x = int(input('Enter First Number\t:\t"));
y = int(input('Enter Second Number\t:\t"));
  
if (oppositeSigns(x, y) == True): 
    print "Signs are opposite"
else: 
    print "Signs are not opposite"
