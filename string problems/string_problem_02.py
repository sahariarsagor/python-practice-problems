'''
Count the number of vowel in a string. 
'''

myName = "sahariar sagor";
vowel = "aeiou";
count = 0;

for a in myName:
    if a in vowel:
        count = count + 1;
print("Number of vowel in your string: ", count);