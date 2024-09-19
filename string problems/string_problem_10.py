'''
    Check if two strings are anagrams (contain the same characters in different order).
'''

s1 = "sahariar";
s2 = "arasarih";

if(sorted(s1) == sorted(s2)):
    print("anagrams");
else:
    print("Not anagrams");