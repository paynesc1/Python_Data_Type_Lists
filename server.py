# generate random list of numbers
import random
"""
generates a random list of numbers
"""
def randoms():
    # make list n long, must be at least digits ling
    my_num = random.randint(1,20)
    rand_list = []
    for i in range(my_num):
        # items in list randonly chosen between 1-5
        n = random.randint(1,5)
        rand_list.append(n)
    return rand_list
result = randoms()
# print(result)


"""
generates a random integer
for problem #10, #20
"""
def random_int():
    number = random.randint(1,15)
    return number
random_integer = random_int()
# print(random_integer)



# # 1. Write a Python program to sum all the items in a list.
# def sum(my_list):
#     sum = 0
#     print(my_list)
#     for i in my_list:
#         sum += i
#     return sum
# print(sum(result))

# 2. Write a Python program to multiply all the items in a list.
# def multiply(my_list):
#     total = 1
#     for i in my_list:
#         total *= i
#     return total
# print(multiply(result))


# 3. Write a Python program to get the largest number from a list.
# def largest(my_list):
#     largest_num = None
#     for i in my_list:
#         if largest_num == None or i > largest_num:
#             largest_num = i
#     return largest_num
# print(largest(result))


# 4. Write a Python program to get the smallest number from a list.
# def smallest(my_list):
#     smallest = None
#     for i in my_list:
#         if smallest == None or i < smallest:
#             smallest = i
#     return smallest
# print(smallest(result))


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# def count_strings(my_list):
#     count = 0
#     for word in my_list:
#         if len(word) > 1 and word[0] == word[-1]:
#             count += 1
#     return count
# print(count_strings(['abc', 'xyz', 'aba', '1221']))


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
#     return n[-1]

# def get_list(my_list):
#     sorted_list = sorted(my_list, key=last)
#     return sorted_list
# print(get_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



# 7. Write a Python program to remove duplicates from a list.
# def duplicates(my_list):
#     # create empty list of duplicates
#     dup = []
#     for i in my_list:
#         print(i)
#         if i not in dup:
#             dup.append(i)
#         else:
#             continue
#     return dup

# print(duplicates(result))


# 8. Write a Python program to check if a list is empty or not.
# def empty_list(my_list):
#     if len(my_list) == 0:
#         return "List is empty"
#     else:
#         return "List is not empty"
# print(empty_list(result))


# 9. Write a Python program to clone or copy a list.
"""
    Use result from the randoms() function at the top
"""
# def clone(list_):
#     my_list = list_.copy()
#     print("The copied list is: ",my_list)
#     return my_list
# print(clone(result))



#10. Write a Python program to find the list of words that are longer than n from a given list of words.
"""
    Use result from random_int to get random integer for func parameter
"""
# def longer_words(n, my_string):
#     # create empty list for words longer than n
#     word_list = []
#     # get random int from top of program
#     print(f"The random integer is", n)
#     # read words.txt doc
#     for line in my_string:
#         words = line.split()
#         for word in words:
#             if len(word) > n:
#                 word_list.append(word)
#     if len(word_list) == 0:
#         print("No words longer than the integer.")   
#     print(f"Words longer then {n}:", word_list)

# # function to get text frmo file as input to above function
# def get_text():
#     with open("words.txt", 'r') as fhand:
#         return fhand.readlines()
        
# longer_words(random_integer, get_text())


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# def common_lists(list_one, list_two):
#     #iterate over one list, if i in the other list return True
#     for i in list_one:
#         if i in list_two:
#             return True
#     return False
    
# # common_lists(randoms(), randoms())


# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# def take_away(list_one):
#     print(list_one)
#     indices_to_remove = [0,4,5]
#     filtered_list = []
#     for index, i in enumerate(list_one):
#         if index not in indices_to_remove:
#             filtered_list.append(i)

#     print(filtered_list)
# take_away(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])



# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
# def my_array():
    
# my_array()


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# def no_evens(my_list):
#     odd_list = []
#     # print(my_list)
#     for i in my_list:
#         if i % 2 == 1:
#             odd_list.append(i)
#     return odd_list
# no_evens(result)


# 15. Write a Python program to shuffle and print a specified list.
# def shuffle_list(my_list):
#     print(my_list)
#     (random.shuffle(my_list))
#     print(my_list)
# shuffle_list(result)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# def first_and_last():
#     # create new list
#     new_list = []
#     # create ist 1-20
#     for i in range(1, 21):
#         new_list.append(i**2)
#     print(new_list[:5])
#     print(new_list[-5:])
# first_and_last()


# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# def prime_check(my_list):
#     print(my_list)
# prime_check(result)

# 18. Write a Python program to generate all permutations of a list in Python.
# from itertools import permutations
# def something(iterable):
#     print(iterable)
#     perm = permutations(iterable)
#     for i in list(perm):
#         print(i)
    
# something([1,2,3])


# 19. Write a Python program to calculate the difference between the two lists.
# def difference(list_one, list_two):
#     print(list_one)
#     print(list_two)
#     sum_one = 0
#     sum_two = 0
#     for i in list_one:
#         sum_one += i
#     for j in list_two:
#         sum_two += j
#     print(sum_one - sum_two)
# difference(randoms(), randoms())

# 20. Write a Python program to access the index of a list.
# def list_index(my_list):
#     print(my_list)
#     count = 0
#     for i in my_list:
#         print(count, i)
#         count += 1
# list_index(result)


# 21. Write a Python program to convert a list of characters into a string.
# def string_list(my_list):
#     print(my_list)
#     my_string = [str(i) for i in my_list]
#     my_string_new = "".join(my_string)
#     print(my_string_new)
#     print(type(my_string_new))
# print(string_list(result))



# 22. Write a Python program to find the index of an item in a specified list.
# def list_index(my_list, random_integer):
#     print(my_list)
#     print(random_integer)
#     if random_integer > len(my_list):
#         print("List not long enough , try again!")
#     else:
#         print(f"List index value is: {my_list[random_integer]}")
# list_index(result, random_integer)



# 23. Write a Python program to flatten a shallow list.

# 24. Write a Python program to append a list to the second list.
# def append_lists(my_list_one, my_list_two):
#     print(my_list_one)
#     print(my_list_two)
#     new_list = my_list_one + my_list_two
#     return (f"Both lists appended: {new_list}")
# print(append_lists(randoms(), randoms()))

# 25. Write a Python program to select an item randomly from a list.
# def select_random(my_list):
#     print(my_list)
#     num = random.randint(0, len(my_list)-1)
#     print(num)
#     return my_list[num]
# print(select_random(result))


# 26. Write a Python program to check whether two lists are circularly identical.


# # 27. Write a Python program to find the second smallest number in a list.
# def second_smallest(my_list):
#     print(my_list)
#     # check that list is not less than 2
#     if len(my_list) < 2:
#         return
    
#     # check that a list lenght equal to 2, both values are not the same
#     if len(my_list) == 2 and my_list[0] == my_list[1]:
#         return
#     # define variables, don't want repeated values, trim list
#     dup_vals = []
#     unique_vals = []

#     for i in my_list:
#         if i not in dup_vals:
#             unique_vals.append(i)
#             dup_vals.append(i)

#     unique_vals.sort()
#     print(unique_vals)
#     print(f"The smallest number is {unique_vals[0]}")
#     print(f"The second smallest number is {unique_vals[1]}")
#     return unique_vals[1]
# print(second_smallest(result))


# 28. Write a Python program to find the second largest number in a list.
# def second_largest(my_list):
#     # check list length
#     if len(my_list) < 2:
#         return
    
#     # check is list length is equal to two and both #'s are the same
#     if len(my_list) ==2 and my_list[0] == my_list[1]:
#         return

#     # set variables
#     dup_items = []
#     unique_items = []
#     print(my_list)
#     for i in my_list:
#         if i not in dup_items:
#             unique_items.append(i)
#             dup_items.append(i)
#     unique_items.sort()
#     print(unique_items)
#     return unique_items[-2]
# print(second_largest(result))


