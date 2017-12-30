def calculate(list):
    sum = 0
    for pos in range(0,len(list)):
        if (type(list[pos]) == list):
            sum = sum + calculate(list[pos])
        else:
            sum = sum + list[pos]
    return sum
def main():
    list = [2,1,[5,6],3,[[1]]]
    sum = calculate(list)
    print('Sum of elements of the list: ',sum)
if(__name__ == '__main__'):
    main()
