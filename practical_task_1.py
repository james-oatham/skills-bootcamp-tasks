""" 
Create parent & child classes, with additional attributes for the child.

Course class (parent):
* Declare the class attributes, with default values.
* Define a method that prints the contact details for the course.
* Define a method that prints the head office location.

OOPCourse class (child):
* Declare additional attributes.
* Define two methods for printing some of the additional attributes.
"""


class Course:

    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"


    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)


    def head_office_details(self):
        print("The head office location is", self.head_office_location)


class OOPCourse(Course):

    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"
    course_id = "#12345"

    def trainer_details(self):
        print(f"The course covers {self.description}; the trainer is {self.trainer}")

    def show_course_id(self):
        print(f"The ID number of the course is {self.course_id}")


# Create an object of the OOPCourse subclass called course_1.
course_1 = OOPCourse()

# Call the following methods.
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()