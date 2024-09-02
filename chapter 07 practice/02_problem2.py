'''
Determine Voting Eligibility 
if age is greater than 18 than he/she eligible for vote and is not than he/she is not for eligible for vote. 
'''

age = int(input("Enter your age: "));

if(age >= 18):
    print(f"your age is: {age} and you are eligible for vote. ");
else:
    print("you are kid not eligible for vote");