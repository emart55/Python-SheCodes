#Store multiple data points - Can take different data types
# digits = [1,2,3,4,5] #string, integer, float, list
# print(digits)
# digits.append(6)
# print(digits)

# popped_element = digits.pop(0)
# print(digits)

# digits[1] = 90
# print(digits)

# print(list_name)
# print(type(list_name))

#print(len(digits)) #Gives you the length of the list

#Lists are index based, which starts from 0.
# print(digits[4])
# print(digits[-1]) #give very last element
#Slicing a list
# print(digits[0:4]) #Start (inclusive) and end index (exclusive) 
# print(digits[-2:5])
# print(digits[0:5:3]) 

#Nested lists = A list within a list
letters = ['a','b','c','d',['Emily','Julie']]
#print(letters[4][0]) #Get the first list, then get the first element from another list

if 'a' in letters:
    print("It is in the list")