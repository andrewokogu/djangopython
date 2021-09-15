#question 1
s1 = "Ault"
s2 = "Kelly"
middleIndex = int(len(s1)/2)
print("Original Strings are", s1,s2)
middle_three = s1[:middleIndex:] + s2 + s1[middleIndex:]
print("The new string after appending in the middle is \n\t\t:", middle_three)


#question 2
s1 = "America"
s2 = "japan"
#output = Ajrpan
first_letters = s1[:1] + s2[:1]
middle_letters = s1[int(len(s1) / 2) :int(len(s1) / 2) + 1] + s2[int(len(s2) / 2) :int(len(s2) / 2)+ 1]
last_letters = s1[len(s1) - 1] + s2[len(s2) - 1]
solution = first_letters + middle_letters + last_letters
print("The new string is \n\t\t:", solution)


#question 3
s1 = "Abc"
s2 = "Xyz"
s2 = s2[::-1]
lengthS1 = len(s1)
lengthS2 = len(s2)
length = lengthS1 if lengthS1 > lengthS2 else lengthS2
result_string =" "
for i in range(length):
  if(i < lengthS1):
      result_string = result_string + s1[i]
  if(i < lengthS2):
      result_string = result_string + s2[i]
print("The new string is \n\t\t", result_string)


s1 = "Abc"
s2 = "Xyz"
print(s1[0]+s2[2]+s1[1]+s2[1]+s1[2]+s2[0])