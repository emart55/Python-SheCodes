#While loops Exercises:
#Question 2-
#Solution 1 = 
# print("The First number is 0")
# large_number = int(input("Enter a number:"))
# while (large_number > 0):
#     if (large_number % 2!= 0):
#         print(large_number)
#     large_number = large_number - 1

#Solution 2 = 
# number=0
# integer_number= int(input("Please enter a number"))

# while number<= integer_number:
#     if number%2==1:
#         print(number)
#     number = number+1



#For loop exercises: 
#Question 1-
# to_multiply = int(input("Give me a number"))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

#Question 2-
# max_number = int(input("Enter a number"))
# total = 0

# for number in range(0, max_number+1):
#     print("This is the variable number first time", number)
#     print(total)
# total += number
# print(number)
# print(total)


# largest_number = int(input("Enter a whole number: "))
# total = 0

# for number in range(0,largest_number+1):
#     total += number

# print(total)




    
#Save a list of numbers to a variable in your script, and then use a for loop to print thesum of all the numbers in the list.
# Question 3 - 
# my_list = [3,5,9,1]

# for number in my_list:
#     print(number)

# number = 0

# while number < 9:
#     print(number)
#     number = number + 1
# print("FINISHED")

#Question 4 - 
# lyrics = [["Monica", "in my life"],    ["Erica", "by my side"],    ["Rita's", "all I need"],    ["Tina's", "what I see"],    ["Sandra", "in the sun"],    ["Mary", "having fun"],    ["Jessica", "here I am"]]

# for lyric in lyrics:
#     print("A little bit of") 
#     print(lyric[0], lyric[1])

# print("A little bit of you makes me your man (ah!)*trumpet solo*")

# iterations = ["first", "second", "third"]
# print("Starting the outer loop!")
# for outer_number in iterations: # outer loop
#     print("Starting the inner loop!")
#     for inner_number in iterations: # inner loop
#         print(f"The outer loop is on its {outer_number} iteration, while theinner loop is on its {inner_number} iteration.")
#     print("Inner loop complete!")

# print("Outer loop complete!")



# groceries = [["Baby Spinach", 2.78],    [
#     "Hot Chocolate", 3.70],    ["BBQ Shapes", 9.00],    ["Bread", 2.10],    ["Carrots", 0.56],    ["Oranges", 3.08]
#     ]

# total_spent = 0

# for grocery in groceries:
#     grocery_amount = int(input(f"How much {grocery[0]} did you buy?: "))

#     total_spent = total_spent + (grocery_amount*grocery[1])
#     print(total_spent)

# print(total_spent)

# from random import randint

# play_the_game = True

# # Question 3-
# def play_game():
#     number = randint(1,10)
#     guess_attempt = int(input("Make a guess! "))

#     while guess_attempt != number:
#         if int(guess_attempt) < number:
#             print("Too low...")
#         else:
#             print("Too high...")
#         guess_attempt = int(input("Make another attempt"))

#     print("You get it right!")
#     play_again = str(input("Do you want to play again?: "))

#     if play_again == "no":
#             global play_the_game
#             play_the_game = False
            
#     return number

# while play_the_game == True:
#     play_game()
