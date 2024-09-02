'''
Calculate Electricity Bill
'''

unit = int(input("Enter unit consumer: "))

if(unit <= 100):
    bill = unit*5;
elif(unit <= 200):
    bill = (100*5) + (unit - 100)*7;
else:
    bill = (100*5) + (100 * 7) + (unit - 200)*10;

print(f"total unit: {unit} and calculated bill: {bill}");