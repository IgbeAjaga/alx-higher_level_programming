#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create an empty list to store the results
    result = []

    # Loop through the original list and check if each element is divisible by 2
    for element in my_list:
        # If the element is divisible by 2, append True to the result list, otherwise append False
        result.append(element % 2 == 0)

    return (result)
