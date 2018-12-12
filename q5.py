#concatenate the string of char in even position
text="innovationwithpython"
h=list(text)
print("String",text)
even = h[1:][::2]
print("Even char in string: " + str(even))