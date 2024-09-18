s = "sahariar sagor";

#count(sbstring): return the number of occurance of a substring in the string. 
print(s.count("s")); # 2 

#startingWith(prefix): return true if the string starts with the specified prefix otherwise false. 

print(s.startswith("s")); #true. 
print(s.startswith("h")); #flase. 

#endswith(prefix): look like startswith

print(s.endswith("r")); # true 
print(s.endswith("s")); # false. 