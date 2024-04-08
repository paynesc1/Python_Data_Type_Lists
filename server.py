# generate random list of numbers
import random
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
print(result)



# # 1. Write a Python program to sum all the items in a list.
# def sum(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
# print(sum(result))

# 2. Write a Python program to multiply all the items in a list.
# def multiply(list):
#     total = 1
#     for i in list:
#         total *= i
#     return total
# print(multiply(result))


# 3. Write a Python program to get the largest number from a list.
# def largest(list):
#     largest_num = None
#     for i in list:
#         if largest_num == None or i > largest_num:
#             largest_num = i
#     return largest_num
# print(largest(result))


# 4. Write a Python program to get the smallest number from a list.
# def smallest(list):
#     smallest = None
#     for i in list:
#         if smallest == None or i < smallest:
#             smallest = i
#     return smallest
# print(smallest(result))


# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# def count_strings(list):
#     count = 0
#     for word in list:
#         if len(word) > 1 and word[0] == word[-1]:
#             count += 1
#     return count
# print(count_strings(['abc', 'xyz', 'aba', '1221']))


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n):
#     return n[-1]

# def get_list(list):
#     sorted_list = sorted(list, key=last)
#     return sorted_list
# print(get_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



# 7. Write a Python program to remove duplicates from a list.
# def duplicates(list):
#     # create empty list of duplicates
#     dup = []
#     for i in list:
#         print(i)
#         if i not in dup:
#             dup.append(i)
#         else:
#             continue
#     return dup

# print(duplicates(result))


# 8. Write a Python program to check if a list is empty or not.
# def empty_list(list):
#     if len(list) == 0:
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