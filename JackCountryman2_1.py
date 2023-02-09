def main():                         #continuous loop
    numStudents = ''
    while numStudents!= -2:
        numStudents = int(input("\n\nTotal number of students: "))
        inScores = []
        if (numStudents > 0):
            while len(inScores) < numStudents:
                inScores = input(f"Enter {numStudents} score(s): ")
                inScores = inScores.split(" ")        
            scores = clean(numStudents, inScores)
            high = max(scores)
            x=1
            for i in scores:
                print(f"Student {x} score is {i} and grade is {grade(high, i)}")
                x = x + 1

def clean(length, list):            #cuts the list down to the number of students and converts to list of ints (week 2 lecture for list indexing)
    fixed = []
    if len(list) > length:
        fixed = list[:length]
    else:
        fixed = list
    fixed = [int(i) for i in fixed]
    return fixed

def grade(high, grade):             #does math to determine letter grade for each student
    letter = ''
    dif = high-grade
    if dif <= 10:
        letter = 'A'
    elif dif > 10 and dif <= 20:
        letter = 'B'
    elif dif > 20 and dif <= 30:
        letter = 'C'
    elif dif > 30 and dif <= 40:
        letter = 'D'
    else:
        letter = 'F'
    return letter

main()
        