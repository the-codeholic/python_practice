class my_class:
    def __init__(self, class_name, strength_of_students):
        self.class_name = class_name
        self.strength_of_students = strength_of_students
        welcome_message = "Welcome to the Class \'" + self.class_name + "\' with \'" + str(
            strength_of_students) + "\' number of students"
        length_welcome_message = len(welcome_message)
        print(welcome_message)
        print(length_welcome_message * "*")

    def ask_what_to_do(self):
        ask = "Enter Option number to do a task"
        length_ask = len(ask)
        print(ask)
        print((length_ask // 4) * "- - ")
        print("1) Enter Student Details ")
        print("2) Enter Mark of the Student")
        print("3) Enter Fee Details")
        print("4) Show Student Details")
        option = input("\tEnter a option(1 2 3 4): ")
        if option == 1:
            self.student_details()
        elif option == 2:
            self.student_mark()
        elif option == 3:
            self.fee_details()
        elif option == 4:
            self.print_details()
        else:
            print("Wrong Input :(")

    def student_details(self):
        print("Selected option is: 1) Enter Student Details")


    def student_mark(self):
        print()

    def fee_details(self):
        print()

    def print_details(self):
        print()


class_name = input("Enter your class name: ")
strength_of_students = int(input("Enter Number of Students: "))

my_class(class_name, strength_of_students)
