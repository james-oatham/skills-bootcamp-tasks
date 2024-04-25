"""
Sum numbers in a given list up to the given index, using recursion.

Access the number in the list at the index stated in the function call,
then work backwards by making recursive calls to add each previous number,
reducing the index number argument by 1 each time.
"""

# Function definition:
    # The 'list_validated' parameter has a default value of False, so that 
    # the list passed to the function is only validated on the first call
    # and not on every recursive call.
def adding_up_to(func_list, func_index, list_validated = False):
    
    """
    Validate the arguments passed and run recursively until complete.
    
    Perform the following validations on the arguments passed:
    * The list is a value of the 'list' data type
    * The index is a whole number (positive numbers only)
    * The index given does not exceed the index for the final element
        otherwise it would be out-of-range
    * The list contains only numbers (up-to-and-including the number at
         the index specified as the second argument;
         any non-numbers after the index won't be evaluated in the calculation)

    The base case is invoked when the start of the list (ie. index 0) has
    been reached (working backwards from the index given), i.e. there are no
    more numbers in the list to add together.
    
    The recursive case adds the number at the current index in the list to 
    the number at the index to the left, by calling the function recursively
    for index-1.
    """

    ### Validation ###

    if type(func_list) != list:
        return "ERROR: Please pass an object of class 'list' as the first argument"

    if type(func_index) != int:
        return "ERROR: The index given is not an integer"

    if func_index < 0:
        return "ERROR: The index given is a negative number"

    if func_index > len(func_list)-1:
        return "ERROR: The index given exceeds the index for the final element"

    # The following validation will only occur on the first function call,
    # to prevent unnecessary processing on each recursive call
    if list_validated == False:
        i = 0
        while i <= func_index:
            if type(func_list[i]) not in (int, float):
                return "ERROR: One or more elements in the list given are non-numerical values"
            i += 1
    

    ### Function code ###

    # Base case:
    if func_index == 0:
        return func_list[0] # Return the number at index 0.
    
    # Recursive case:
    else:
        # Pass 'True' for recursive call to avoid re-validating the list.
        return func_list[func_index] + adding_up_to(func_list, func_index-1, True)
    
# Call the function and print the result.
# Do not include an argument for the 'list_validated' parameter.
print(adding_up_to([1,2,3,4,5],4))