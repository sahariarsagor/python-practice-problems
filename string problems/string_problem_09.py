'''
    Remove all punctuation from a string.
'''
import string;
s = "sahariar, sagor!";
clean_string = "";

for char in s:
    if char not in string.punctuation:
        clean_string += char;
print(clean_string);