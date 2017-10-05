def areaTriangle(base , height):
    '''
        objective : to compute the area of the Triangle
        input parameters : 
            base : Base of Triangle 
            height : Height of Triangle
        approach  : multiply base and height
        return value : area of Triangle
    '''
    area=0.5 * base * height
    return area

def main():    
    '''
        objective : to compute the area of the Triangle
        user inputs : 
            base : Base of Triangle 
            height : Height of Triangle
        approach  : to use function areaTriangle()
        return value : area of Triangle
    '''
    base = int(input("Enter base of Triangle "))
    height =int(input("Enter height of Triangle "))
    print('base of Triangle : ', base)
    print('height of Triangle : ',height)
    print('Area of Triangle : ', areaTriangle(base ,height))
    
if __name__ == '__main__':
    main()
print("End of the Program")
