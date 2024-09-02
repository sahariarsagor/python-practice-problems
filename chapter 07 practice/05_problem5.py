'''
Grade Calculator: 
conditions: 
accept mark. 
and use bd university grading system.
'''

mark = int(input("Enter your marks: "))

#Conditions: 
if(mark < 40 and mark > 0):
    print("Try again dont give  up go got failed.");
elif(mark >= 40 and mark < 50):
    print("you got D in Examination. ");
elif(mark >= 50 and mark < 55):
    print("You got C in the Exam. ");
elif(mark >= 55 and mark < 60):
    print("You Got C+ in the exam");
elif(mark >= 60 and mark < 65):
    print("You Got B in the exam");
elif(mark >= 65 and mark < 70):
    print("You got B+ in the exam ");
elif(mark >= 70 and mark < 75):
    print("You got A- in the exam.");
elif(mark >= 75 and mark <= 80):
    print("You got A in the exam. ");
elif(mark > 80 and mark <= 100):
    print("You got A+ in the examination");
elif(mark > 100):
    print("Such a invald number");
else:
    print("Something went wrong please try again");