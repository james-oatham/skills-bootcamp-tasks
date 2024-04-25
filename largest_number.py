"""
Return the largest number from a given list, using recursion.

Access the number in the list for the current index value and then
call the function recursively for the number at the next index,
returning the max of the two.
"""

# Function definition:
    # The 'func_index' parameter has a default value of 0 so that it starts
        # at the beginning of the list on the first call, without needing to be
        # explicit in the function call.
    # The 'list_validated' parameter has a default value of False, so that
        # the list passed to the function is only validated on the first call and
        # not on every recursive call.

def largest_number(func_list, func_index = 0, list_validated = False):

    """
    Validate the arguments passed and run recursively until complete.
    
    Perform the following validations on the arguments passed:
    * The list is a value of the 'list' data type
    * The list contains only numbers
    
    The base case is invoked when the end of the list has been reached, i.e.
    index = list length - 1. Therefore, this is the last number to consider
    as the largest.

    The recursive case returns the max of the current number and the next
    number in the list, by calling the function recursively for index + 1.
    
    """
    ### Validation ###

    if type(func_list) != list:
        return "ERROR: Please pass an object of class 'list' as the first argument for this function"

    if list_validated == False:
        for i in func_list:
            if type(i) not in (int, float):
                return "ERROR: One or more elements in the list given are non-numerical values"


    ### Function code ###
    
    # Base case:
    if func_index == len(func_list)-1:
        return func_list[func_index] # Return the number at the current (final) index
    
    # Recursive case:
    else:
        return max(func_list[func_index], largest_number(func_list, func_index+1, True))

# Call the function and print the result.
# Do not include arguments for the 'func_index' or
    # the 'list_validated' parameters.
print(largest_number([1,3,6,8,7,2,14]))