                    
                    
                    
                    
                    
                    
                    
                    
E = int(input("Enter the total number of students that subscibed to an English newspaper:\n"))
English = set(input("enter their roll numbers:\n").split())
F = int(input("Enter the total number of students that subscibed to a French newspaper:\n"))
French = set(input("Enter their roll number:\n").split())
final = English.intersection(French)
print(final)
print(len(final))



