str1 = "HELLO WORLD"
print(str1.isupper())  # output: True
str2 = "Hello World"
print(str2.isupper())  # output: False
str3 = "HELLO123"
print(str3.isupper())  # output: False (contains digits)
str4 = "HELLO WORLD!"
print(str4.isupper())  # output: True (contains punctuation)