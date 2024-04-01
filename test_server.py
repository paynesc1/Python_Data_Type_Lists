# pip install pytest
from server import smallest

# ***************************************** #

 # 1. Write a Python program to sum all the items in a list.
# def test_sum():
#     test_cases = [
#         ([5,3], 8),
#         ([-4,-6],-10),
#         ([7,0], 7),
#         ([999999,1], 1000000),
#     ]
#     for input_list, expected in test_cases:
#         assert sum(input_list) == expected, f"Add ({input_list}) should equal ({expected})"

# ***************************************** #

# 2. Write a Python program to multiply all the items in a list.
# def test_multiply():
#     # Define your test cases as a list of tuples (input_list, expected_result)
#     test_cases = [
#         ([2, 3, 4], 24),
#         ([1, 2, 3, 4, 5], 120),
#         ([1, -1, 1, -1], 1),
#         ([10], 10),
#         ([], 1)  # Testing multiplication with an empty list should return the identity element, 1
#     ]
    
#     # Iterate over each test case
#     for input_list, expected in test_cases:
#         # Use assert statement to check if multiply function's output matches the expected result
#         assert multiply(input_list) == expected, f"multiply({input_list}) should equal {expected}"

# ***************************************** #

# 3. Write a Python program to get the largest number from a list.
# def test_largest():
#     test_cases = [
#         ([2, 3, 4], 4),
#         ([1, 2, 3, 4, 5], 5),
#         ([1, -1, 1, -1], 1),
#         ([10], 10),
#     ]
#     for input_list, expected in test_cases:
#         assert largest(input_list) == expected, f"Largest in ({input_list}) should be ({expected})"

# ***************************************** #

# 4. Write a Python program to get the smallest number from a list.
def test_smallest():
    test_cases = [
        ([5, 3, 4, 1, 2], 1),
        ([-2, -6, -3, -8, -4], -8),
        ([1, 2, 3, 4, 5], 1),
        ([5], 5),
        ([], None),
    ]
    for input_list, expected in test_cases:
        assert smallest(input_list) == expected, f"Smallest in ({input_list}) should be ({expected})"
