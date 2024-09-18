myName = "sahariar,sagor";

#split(): Split a string into a list and where each word is a list item. 
print(myName.split(","));
print("Hello,World".split(","));

#join(): join element of an iterable, 
word = "Hello", "Sahariar";
print("-".join(word)); #Hello-Sahariar. 

#find(substring): Return the index of the first occurance of the subsrting return (-1) if the substring is not found. 

s = "hello sahariar";
print(s.find("s")); # 6 
print(s.find("z")); # -1 