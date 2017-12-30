class Person:
    ''' The class Person describes a person'''
    count=0
    def __init__(self , name , DOB , Address ):
        '''
        Objective: To initialize object of class Person
        Input Parameters:
            self (implicit parameter) - object of type Person
            name - string
            DOB - string (Date of Birth)
            address - string
        Return Value: None
        '''
        self.name=name
        self.DOB=DOB
        self.Address=Address
        Person.count+=1

    def getName(self):
        '''
        Objective: To retrieve name of the person
        Input Parameter: self (implicit parameter) - object of type Person
        Return Value: name - string
        '''
        return self.name
    
    def getDOB(self):

         '''
        Objective: To retrieve the date of birth of a person
        Input Parameter: self (implicit parameter) - object of type Person
        Return Value: DOB - string
        '''
         
         return self.DOB

    
    def getAddress(self):
         '''
        Objective: To retrieve address of person
        Input Parameter: self (implicit parameter) - object of type Person
        Return Value: address - string
        '''
         return self.Address
    
    def getCount(self):
        '''
        Objective: To get count of objects of type Person
        Input Parameter: self (implicit parameter) - object of type Person
        Return Value: count: numeric
        '''
        return Person.count

    def setName(self , name):
        '''
        Objective: To update name of person
        Input Parameter: self (implicit parameter) - object of type Person
        name – string value
        Return Value: None
        '''
        self.name=name

    def setDOB(self , DOB):
        '''
        Objective: To update DOB of person
        Input Parameter: self (implicit parameter) - object of type Person
        DOB – string value
        Return Value: None
        '''
        self.DOB=DOB

    def setAddress(self , Address):
        '''
        Objective: To update address of person
        Input Parameter: self (implicit parameter) - object of type Person
        address – string value
        Return Value: None
        '''
        self.Address=Address
        
    def __str__(self):
        '''
        Objective: To return string representation of object of type Person
        Input Parameter: self (implicit parameter)- object of type
        Person
        Return Value: string
        '''
        return 'Name:'+self.name+'\nDOB:'+str(self.DOB)\
        +'\nAddress:'+self.address

    def __del__(self):
        '''
        Objective: To be invoked on deletion of an instance of the
        class Person
        Input Parameter:
        self (implicit parameter) – object of type Person
        Return Value: None
        '''
        print('Deleted !!')
        Person.count -= 1
