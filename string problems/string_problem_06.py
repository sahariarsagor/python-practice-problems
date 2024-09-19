'''
    Find the longest word in a string. 
'''

s = "hi i am sahariar sagor and i love programming";
words = s.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word;
print(longest) 