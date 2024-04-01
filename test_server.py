# pip install pytest
from server import multiply


def test_multiply():
    # Define your test cases as a list of tuples (input_list, expected_result)
    test_cases = [
        ([2, 3, 4], 24),
        ([1, 2, 3, 4, 5], 120),
        ([1, -1, 1, -1], 1),
        ([10], 10),
        ([], 1)  # Testing multiplication with an empty list should return the identity element, 1
    ]
    
    # Iterate over each test case
    for input_list, expected in test_cases:
        # Use assert statement to check if multiply function's output matches the expected result
        assert multiply(input_list) == expected, f"multiply({input_list}) should equal {expected}"