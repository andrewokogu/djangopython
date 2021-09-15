s1 = "Abc"
s2 = "Xyz"
#print(s1[0]+s2[2]+s1[1]+s2[1]+s1[2]+s2[0])


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