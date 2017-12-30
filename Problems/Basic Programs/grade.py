def assignGrade(marks):
    '''
    Objective: To assign grade on the basis of marks obtained
    Input Parameter: marks – numeric value
    Return Value: grade - string
    '''
    assert marks >= 0 and marks <= 100
    if marks >= 90:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def main():
    '''
    Objective: To assign grade on the basis of input marks
    Input Parameter: None
    Return Value: None
    '''
    marks = float(input('Enter your marks: '))
    print('Marks:', marks, '\nGrade:', assignGrade(marks))

if __name__=='__main__':
    main()
