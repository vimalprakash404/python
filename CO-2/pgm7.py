# Add the 'ing' at the end of the given string, if it already ends with 'ing',then add 'ly'

str = input("Enter a string:")
if str.endswith("ing"):
    str = str + "ly"
else:
    str = str + "ing"
print("modified string is:", str)

# method 2

# if s[-3:]=="ing":
#     print(s+"ly")
# else:
# print(s+"ing")
