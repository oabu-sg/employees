#   Read how many employees you need to enter
employee_count_str = input("Please enter how many employees you wish to enter:")

employee_count = int(employee_count_str)

#   Loop through employees
total_age = 0
for employee_index in range(employee_count):
    #   Read first name, last name and age

    while True:
        first_name = input("Please Enter The First Name:")
        if len(first_name.strip()) > 0:
            break

    while True:
        last_name = input("Please Enter The Last Name:")
        if len(last_name.strip()) > 0:
            break

    while True:
        age_str = input("Please Enter the Age:")

        if age_str.isdigit():
            age = int(age_str)
            if (age >= 18) and (age <= 100):
                total_age = total_age + age
                break
            else:
                print("The age should be a digit between 18 and 100")
        else:
            print("The age should contain only digits")

    print(f"Employee Data: First Name: {first_name}, Last Name: {last_name}, Age: {age}")
    print(f"Total Age = {total_age}")

if total_age > 500:
    print("Warning: the total age for all employees is more than 500")
else:
    print("Warning: the total is less than 500")

