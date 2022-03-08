def print_line(text = "Default Value"):
    print("--------------- INPUT ---------------" + text)

def read_name(name_type):
    while True:
        print_line("Reading a Name")
        name_var = input(f"Please Enter The {name_type}:")
        if len(name_var.strip()) > 0:
            #break
            return name_var

    #return name_var

'''
def read_last_name():
    while True:
        last_name = input("Please Enter The Last Name:")
        if len(last_name.strip()) > 0:
            break
    return last_name
'''

def read_age():
    while True:
        print_line()
        age_str = input("Please Enter the Age:")
        if age_str.isdigit():
            age = int(age_str)
            if (age >= 18) and (age <= 100):
                # break
                return age
            else:
                print("The age should be a digit between 18 and 100")
        else:
            print("The age should contain only digits")
    #return age

if __name__ == '__main__':
    #   Read how many employees you need to enter
    print_line("Employee Count")
    employee_count_str = input("Please enter how many employees you wish to enter:")

    employee_count = int(employee_count_str)

    #   Loop through employees
    total_age = 0
    for employee_index in range(employee_count):
        #   Read first name, last name and age

        first_name = read_name("First Name")

        last_name = read_name("Last Name")

        age = read_age()

        total_age = total_age + age

        print(f"Employee Data: First Name: {first_name}, Last Name: {last_name}, Age: {age}")
        print(f"Total Age = {total_age}")

    if total_age > 500:
        print("Warning: the total age for all employees is more than 500")
    else:
        print("Warning: the total is less than 500")

