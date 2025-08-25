str1 = "helllo world"
print(str1.islower())  # output: True
str2 = "Hello World"
print(str2.islower())  # output: False
str3 = "hello123"
print(str3.islower())  # output: False (contains digits)
str4 = "hello world!"
print(str4.islower())  # output: True (contains punctuation)