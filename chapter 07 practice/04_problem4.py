'''
check if a number is positive negetive or zero. 
'''

n = int(input("Enter a number except fraction: "))

if(n>0):
    print("Given number is Positive. ");
elif(n<0):
    print("Given Number is: Negetive. ");
elif(n == 0):
    print("You enter 0");
    
else:
    print("Something went wrong. ");