'''
Check divisibility by 5 and 11. 
'''

n = int(input("Enter number for testing: "))

if(n%5 == 0 and n%11 == 0):
    print(f"{n} is divisible by 5 and 11");
else:
    print(f"{n} is not divisible by 5 and 11");