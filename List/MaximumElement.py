def Max(a,b):
if a>=b:
  return a
else:
  return b
  
def MaxList(l):
 if l==[]:
   return 'null'
 elif len(l)==1:
   return l[0]
 else
   return Max(l[0],MaxList(l[1:])
  
