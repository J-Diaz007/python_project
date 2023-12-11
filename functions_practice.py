###############PART 2################################
## * COMPLETE THE FOLLOWING FUNCTIONS
# # A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
# def hello():
#     print("Sup Y'all?!")

# hello()

# # A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
# def pack(a,b,c):
#     return [a,b,c]

# print(pack("a", "b", "c"))
# print(pack(1,2,3))

# # A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
# def eat_lunch(my_lst):
#   if len(my_lst) == 0:
#     print("My lunchbox is empty!")
#   else:
#     for i in range(len(my_lst)):
#       if i == 0:
#         print(f"First I eat {my_lst[0]}")
#       else:
#         print(f"Then I eat {my_lst[i]}")

# eat_lunch(["sushi"])
# eat_lunch(["oreos","ramen","burgers","ice cream"])
# eat_lunch([])

## * PART 3
## * COMPLETE THE FOLLOWING FUNCTIONS
# # 1. name_args — Accepts any number of named arguments and prints them in the pattern key : value one at a time.

# def name_args(**kwargs):
#   for k in kwargs.keys():
#     print(f"{k}:{kwargs[k]}")

# name_args(name="Randon", weather="sunny",location="park",time=3)
# # 2. all_true — Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

# def all_true(iter):
#   return all(iter)

# print(all_true([True,True,True]))
# print(all_true((True, False)))

# # 3. one_true — Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

# def one_true(iter):
#   return any(iter)

# print(one_true([True,True,True]))
# print(one_true([False, False, False]))
# print(one_true((True, False)))

# # 4. recursive_factorial — Uses recursion to find the factorial of an integer.

# def recursive_factorial(n):
#   if n <= 1:
#     return 1
#   else:
#     return n * recursive_factorial(n-1)

# print(recursive_factorial(3))
# print(recursive_factorial(6))

# # 5. recursive_deduplicate — Recursively removes all adjacent duplicate letters from a string.

# def recursive_deduplicate(my_str,i=0):
#   # if our string is empty or only has 1 thing, it's got no duplicates
#   # if i is at the end of the string, no duplicates are left
#   if len(my_str) <= 1 or i == len(my_str)-1:
#     return my_str
#   else:
#     # str at current position is same as next position
#     if my_str[i] == my_str[i+1]:
#       return recursive_deduplicate(my_str[0:i]+my_str[i+1:],i)
#     else:
#       #no duplicate at current position, check next
#       return recursive_deduplicate(my_str,i+1)
      
# print(recursive_deduplicate("aaaa"))
# print(recursive_deduplicate("aaba"))
# print(recursive_deduplicate("apple"))
# print(recursive_deduplicate(""))

# # 6. recursive_reverse — Uses recursion to reverse a string.
# def recursive_reverse(str, i=0):
#   #empty string case
#   if len(str)==0:
#     return ""
#   #base case
#   elif i == len(str)-1:
#     return str[0]
#   else:
#     #recursive case
#     return str[-1-i] + recursive_reverse(str, i+1)

# print(recursive_reverse("aaaa"))
# print(recursive_reverse("aaba"))
# print(recursive_reverse("apple"))
# print(recursive_reverse(""))
  

## * PART 4
## Write the Following Functions
# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
  # if list is empty, return 0
  if len(list) == 0:
    return 0
  # product starts with first element of the list
  prod = list[0]

  # goes through the list elements and multiplies them together
  if len(list) > 1:
    for i in list[1:]:
      prod = prod * i

  return prod

print(mult_list([1,2,3,4,5]))
print(mult_list([]))
print(mult_list([10,0,100]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(my_str):
  return my_str[::-1]

print(rev_string(""))
print(rev_string("redrum"))
print(rev_string("radar"))

# Write a Python function called num_within() to check whether a number falls in a given range.
  # The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
  # Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
  # The function accepts the number n, the number of rows to print
  # Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)