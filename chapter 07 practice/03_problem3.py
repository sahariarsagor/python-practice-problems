'''
Find the Largest of Three Numbers
a = userinput number;
b = userinput number;
c = user input number;
'''

a = int(input("Enter first number: "));
b = int(input("Enter Second Number: "));
c = int(input("Enter Third Number: ")); 

if(a>b and a>c):
    print("a is greater than all");
elif(b>a and b>c):
    print("b is greater than all");
else:
    print("c is greater than all");