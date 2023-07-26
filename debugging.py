############DEBUGGING#####################

# # Describe Problem
# # the loop uses a range function that takes two numbers , the start and the end (excluding the end number.)
# # That' why the print statement never triggers because i never equals 20 since the end number isnt included in the range
# # solve by changing the end number in range to 21
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# # the problem is that the randint function is being used with 1 and 6 as the range, which then gets used to access an element from the array of images
# # the solution is changing the range to 0 and 5 so that die 1 gets shown and so that it doesnt error out trying to acces something out of the range
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# # The issue is that if comparison only acounts for the years in between 1980 and 1994 with outh including those numbers
# # The solution to the issue is to change > to >= elif comparison
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
#  Issue was that the input user input wasnt being converted to a int so the if satatemnet wasnt able to compare
#  Also there wasnt an f string being used in the print statement so the variable name was being printed
#  the solution was to convert the user input into an integer and then adding an f to the print statement
# age = int(input("How old are you? "))
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# The issue was that the user input for word_per_page was being compared instead of assigned to the variable word_per_page
#  The solution was to change the == to a single = so that the computer knows to reassign the value of the variable
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
print(pages)

total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])