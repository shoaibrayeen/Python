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


def sentence(list1,list2,list3):
    list = []
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            for k in range(0,len(list3)):
                list.append(list1[i]+' '+list2[j]+' '+list3[k])
                
    return list



def main():
    list1 = ['I','You','Archita']
    list2 = ['love','like']
    list3 = ['football','kdrama','coding']
    finallist = []
    finallist = sentence(list1,list2,list3)
    print(*finallist,sep='\n')

if(__name__ == '__main__'):
    main()
