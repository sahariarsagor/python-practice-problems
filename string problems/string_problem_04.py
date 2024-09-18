'''
Count the occurrences of each character in a string.
'''

s = "sahariar";
freq = {};

for char in s:
    if char in freq:
        freq[char] += 1;
    else:
        freq[char] = 1;
print(freq); 