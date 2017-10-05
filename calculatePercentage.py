def calculatePercentage(obtained , maximum):
    '''
        objective : to compute the percentage
        input parameters : 
            obtained : Obtained Marks 
            maximum :  Maximum Marks
        approach  : divide obtained marks by maximum marks and the multiply by 100.
        return value : Percentage of Marks
    '''
    percentage= ( obtained / maximum ) * 100
    return percentage

def main():    
    '''
        objective : to compute the percentage
        user inputs : 
            obtained : Obtained Marks 
            maximum :  Maximum Marks
        approach  : to use function calculatePercentage()
        return value : Percentage of Marks
    '''
    obtained = int(input( "Enter Obtained Marks "))
    maximum =int(input("Enter Maximum Marks "))
    print('Obtained Marks : ' , obtained )
    print('Maximum Marks : '  , maximum )
    print('Percentage of Marks : ' , calculatePercentage( obtained , maximum ))
    
if __name__ == '__main__':
    main()
print("End of the Program")
