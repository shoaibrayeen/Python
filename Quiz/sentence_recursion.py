'''
This Program takes three lists of strings and produces output as 	below.
Input: List of subject, verb and object 
Output: prints all the possible statements of 3 words  
        where word1 is from subject list,
        and word2 is from verb list, 
        and word3 is from object list, followed by a full stop
        
Sample – 
Input lists - 
Subject = [‘I’, ‘You’]
verb = [‘like’, ‘love’]
object = [‘football’, ‘programming’]

Output –
I like football.
I like programming.
I love football.
I love programming.
You like football.
You like programming.
You love football.
You love programming.
'''


def sentence(list1,list2,list3,list4=[],i=0,j=0,k=0):
    if i==len(list1) and j==len(list2) and k==len(list3) :
        return list4
    else:
        if i!=len(list1):
            if j!=len(list2):
                
                if k!=len(list3):
                    list4.append(list1[i]+' '+ list2[j]+' ' +list3[k])
                    return sentence(list1,list2,list3,list4,i,j,k+1)
                else:
                    k=0
                    return sentence(list1,list2,list3,list4,i,j+1,k)
            else:
                j=0
                return sentence(list1,list2,list3,list4,i+1,j,k+1)

        return list4
                            



    
def main():
    list1 = ['I','You','We','They']
    list2 = ['love','like']
    list3 = ['football','kdrama','coding']
    finallist = []
    finallist = sentence(list1,list2,list3)
    print(*finallist,sep="\n")

if __name__ == '__main__':
    main()
