#   Read how many employees you need to enter
employee_count_str = input("Please enter how many employees you wish to enter:")

employee_count = int(employee_count_str)

#   Loop through employees
for employee_index in range(employee_count):
    #   Read first name, last name and age
    first_name = input("Please Enter The First Name:")

    last_name = input("Please Enter The Last Name:")

    age_str = input("Please Enter the Age:")

    age = int(age_str)

    print(f"Employee Data: First Name: {first_name}, Last Name: {last_name}, Age: {age}")
#   Check that first name, last are not empty

#   Check that employee age is between 18 and 100

#   Check the total ages isn't more than 500
