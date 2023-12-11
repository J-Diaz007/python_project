#Section 1 - sets and tuples:
#Pre-Question: Take a look at this JavaScript Array:
# let javaScriptArray = [12, 55, 33, 40, 55, 33, 20, 12]

# How would you remove duplicates from this JavaScript Array? Take a few minutes to consider what steps are necessary to iterate through this array in JavaScript and remove the duplicates values.

# What advantages are available when we're working with Python? If this Array was instead a set, we wouldn't be able to store multiple values in it. Uncomment the identical set below and run the print statement. What did you notice in the console return?

my_set = {12, 55, 33, 40, 55, 33, 20, 12}

print(my_set)

#Question 1a: Create a set of your own with at least 3 different elements.
my_set2 = {"a","b","c"}
#Question 1b: Add an item to the set that you just created.
my_set2.add("d")
#Question 1c: Print the set with the new data that you added to it:
print(my_set2)

#Question 2a: Create a tuple with at least 3 elements inside of it.
my_tup = (1,2,3)
#Question 2b: Print the tuple you just created.
print(my_tup)



#Section 2 - loops:

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Question 3: Use a for loop to iterate through the 'days' list above and print the days of the week:

for day in days:
    print(day)

x = 10
add_list = [10, 6, 12, 4, 5]
# Question 4: Uncomment the list and variable x above.  Loop through add_list and add each value to x. Print the value of x at each increment:

x = 10
for i in add_list:
    x += i
    print(i)

# Question 5: While Loops 

#Declare an iterator variable (set to the number 1) and write a While loop that adds 5 to the value of the variable starting_value as long as the iterator is under 10:

starting_value = 5

i = 1
while i < 10:
  starting_value += 5
  print(starting_value)
  i += 1


#Section 3 - conditionals: if, elif, else statements

favorite_movie = "Encanto"    
#Question 6a: Uncomment the favorite_movie variable above and change the value to the title of your favorite movie
#Below, write a conditional statement that prints the string "that's a great movie" if the favorite_movie variable equals your favorite movie.
#Otherwise (else), print the string "that's not my favorite movie".  
#Mess around with the value of the favorite_movie variable and trigger both conditional responses:
if favorite_movie == "Encanto":
    print("That's a great movie")
else: 
    print("That is not my favorite film")


#Question 6b: Uncomment the movie_list variable below and implement a for loop that iterates through each item in the list. 
#If the item is a blueberry (or another fruit), print "item is a fruit and not movie"; 
#if the item is a car manufacturing company like Toyota, print "item is a car and not a movie"; 
#otherwise, just print the movie in the list:

movie_list = ["Inception", "blueberries", "Toyota", "Good Will Hunting"]

for movie in movie_list:
    if movie == "blueberries":
        print("That's a fruit, not a movie")
    elif movie == "Toyota":
        print("That's a car, not a movie")
    else:
        print(movie)


#BONUS - conditional and operators practice:
a = 5
b = 5
c = 12
#Question 7a: Use the correct operator to add variables a & c:
print(a+c)
#Question 7b: Use the correct operator to subtract variables b & c:
print(b-c)
#Question 7c: Use the correct comparison operator that shows if variables a & b equal each other:
print(a == b)
#Question 7d: Use the correct operator to find the quotient of variables c & a
print(c/a)
#Question 7e: Use the correct operator to find if variables c & b are not equal to each other:
print(c != b)
