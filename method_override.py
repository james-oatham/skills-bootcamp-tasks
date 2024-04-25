"""
Return if a person is old enough to drive based on the age given.

Perform the following actions:
* Ask the user to input a number of different attributes
* Validate each input based on its expected data type
* Create an object in the Adult or Child class based on the age entered
* Call a method to display if the person is old eough to drive
* The method in the parent class is overridden by that in the sub class

PLEASE NOTE:
The attributes to capture are defined in a dictionary; as such, the 
parameters passed in the object creation are seen by Python to be 
undefined, hence "Problems" flagged in VS Code.
"""

driving_age_ZA = 18


# Create class Adult with certain attributes and a single method.
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        if self.age >= driving_age_ZA:
            driving_text = ""
        else:
            driving_text = "not "

        print(f"{self.name} is {driving_text}old enough to drive in South Africa")


# Create a subclass of the Adult class; override the can_drive() method.
class Child(Adult):

    def can_drive(self):
        print(f"{self.name} is too young to drive in South Africa")


def validate_user_input(user_input, data_type):
    """
    Validate user inputs based on the required data type for each input:
    * 'int' data type: must be a positive integer
    * 'str' data type: an input must be given; user cannot just press ENTER
    """
    error_text_int = "Please enter a whole number greater than or equal to 0"
    error_text_str = "You did not enter a value, please try again"

    if data_type == "int":
        try:
            user_input = int(user_input)

            if user_input >= 0:
                return True
            else:
                return error_text_int
            
        except ValueError:
            return error_text_int
        
    else:
        if len(user_input) > 0:
            return True
        else:
            return error_text_str


# Dictionary of attributes and their data types re. input validation.
person_attributes = {
    "name": "str",
    "age": "int",
    "eye_colour": "str",
    "hair_colour": "str"
    }

# Loop through the attributes to capture and validate the inputs.
for i in person_attributes.keys():
    while True:
        vars()[i] = input(f"Please enter the person's {i.replace("_"," ")}: ")

        # Call the validation function and capture the value returned
        valid_input = validate_user_input(vars()[i], person_attributes[i])

        if valid_input == True:
           break

        else:
            print(valid_input)  # Print the error message returned.


### Create an object of the Adult or Child class based on the age ###

# Convert the age inputted by the user from a string to an int;
# the validation function has proved that it can be converted.
age = int(age)

if age >= 18:
    vars()[name.lower()] = Adult(name, age, eye_colour, hair_colour)

else:
    vars()[name.lower()] = Child(name, age, eye_colour, hair_colour)

# Call the can_drive() method.
vars()[name.lower()].can_drive()