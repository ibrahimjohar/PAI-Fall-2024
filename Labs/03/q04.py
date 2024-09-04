#name: ibrahim johar farooqi
#date: 4 september 2024
#lab: 03
#task: 4

def FileEmployeeDatabaseEntry(filename):
    try:
        print("employee details: ")
        name = str(input("enter name: "))
        cnic = int(input("enter cnic number: "))
        age = int(input("enter age: "))
        salary = int(input("enter salary: "))

        with open(filename, 'w') as file:
            file.write(f"Name: {name}\n")
            file.write(f"CNIC number: {cnic}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Salary: {salary}\n")
        
        with open(filename, 'r') as file2:
            content = file2.read()
        print(f"\nfile content:\n{content}")

        contactnum = int(input("enter contact number: "))

        with open(filename, 'a') as file3:
            file3.write(f"Contact Number: {contactnum}\n")

        with open(filename, 'r') as file4:
            updated_content = file4.read()
        print(f"\nfile content after append:\n{updated_content}")

    except FileNotFoundError:
        print("the file does not exist/not found.")
    except IOError:
        print("an error occured during reading the file")
    except Exception as e:
        print(f"unexpected error occured: {e}")

filename = "task4text.txt"
FileEmployeeDatabaseEntry(filename)
