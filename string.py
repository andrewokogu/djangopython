#string indexing and slcing
Firstname ="EJIRO"
Lastname ="Okogu"
Fullname = Firstname + " " + Lastname
print(Fullname [0:11])
#print(Fullname [-5:]) #string slicing

Firstname ="EJIRO"
Lastname ="Okogu"
Fullname = Firstname + " " + Lastname
print(Fullname [7:13])
#print(Fullname [-5:])

#string formatting
#f is for formatting
#name = "Desmond"
#print(f"welcome {name}")

#name = "Ejiro"
#price = 20
#print(f"Welcome {name}. you are to pay {price} ")

#another way to use formatting
#name = "Ejiro"
#print ("welcome {}. you have just signed in".format(name))

#name = input("Tell us who you are: ")
#print ("welcome {}.you have just signed in".format(name))

#name = input("what is your name:" )
#age = int(input(" what is your age:" ))
#year = 2021 - age
#print ("welcome {}.you were born in ".format(year))

#string methods

#name = "MY FILE.PDF".upper()
#print(name)
#print(name.endswith("pdf"))

#fullname = "Ejiro Andrew Okogu"
#name_list = fullname.split()
#print(name_list[1])

#word_list = ['Ejiro', 'Andrew', 'Okogu']
#joined = "-".join(word_list)
#nprint(joined)

#statement = " i am a boy "
#state_list = statement.split()
#joined = "-".join(state_list)
#print(joined)

#word = "i am a boy"
#new_word = word.replace(" ","-")
#print(new_word) #same thing using replace


quote = input("Please enter input")
new_quote = quote.replace("am", "AM")
print(new_quote)
print(new_quote.count(quote))
#print(quote.upper())

