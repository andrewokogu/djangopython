                                #classwork
                                
#write functions to calculate the following statistical measures
#mean, median, mode, standard deviation, variance = standard deviation^2
#find prime numbers

# lst_numbers = [1,2,4,4,5,6,7,8,9,10]

# def mean(data_numbers):
#     return (sum(data_numbers)/len(data_numbers))
# print(mean(lst_numbers))    


# def median(data_numbers):
#     data = sorted(data_numbers)
#     index = len(data) // 2
#     if len(data_numbers) % 2 != 0:
#         return(data)[index]
#     else:
#         return(data[index-1]+ data[index])/2
# print(median(lst_numbers))

#median Mr desmond correction
# def median(num):
#     sorted(num)
#     if len(num)%2==0:
#         mid_point = len(num)//2
#         first = num[mid_point]
#         second = num[mid_point]
#         return(first+second)/2
#     else:
#         mid_point = len(num)//2
#         return num[mid_point]


# def mode (data_numbers):
#     frequency = {}

#     for i in data_numbers:
#         if not i in frequency:
#          frequency[i] = 1

#         else:
#          frequency[i] += 1 
#     return [g for g,l in frequency.items() if l ==max(frequency.values())]          
# print(mode(lst_numbers))

#mode mr desmond solution
# def mode(num):
#     freq = {}
#     for i in num:
#         if i in freq.keys():
#             freq[i]+=1
#         else:
#             freq[i]=1
#     max_key = max(freq, key=freq.get) #max inbuilt method
#     return max_key 
# print(mode(lst_numbers))   

# standard deviation
# def std(num):
#     m = mean(num)
#     return ((sum([lst_numbers - m for a in num]))**2/len(num))**0.5

# #variance
# def variance(num):
#     st = std(num)
#     return st**2

# #prime number
# def prime(num):
#     if num <= 1:
#         return False
#     if num ==2:
#         return True
#     for i in range(2, num):
#         if num % i ==0:
#             return False
#     return True

# #prime numbers function using lambda
# def prime_in_list(num):
#     return list(filter(lambda x: prime(x), num))     




#                                 filei/o

myfile = open('ejiro.txt', mode='w')

# myfile.write("this is the file i just wrote") #writes a string to file

myfile.writelines(['this is line 1\n','this is line 2\n', '\tthis is a tab.'])# this writes a list of strings in the list to the file

#to append to a file
#it appends if theres a tab in your previous write string

#read file
# texts = myfile.read()
# print(texts)

# readlines
# texts = myfile.readlines()
# for text in texts:
#     print(texts)