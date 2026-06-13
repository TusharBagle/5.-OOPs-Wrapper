print("\n--- Python OOP Project : Employee Management System ---")

L1 = [ ]


class Person : 

    def Create_Person (self) :

        global  L1

        while True :

            Person_name = input("\n\n\tEnter the Person Name : ")

            if ( Person_name.isalpha() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Person_age = input("\n\tEnter the Person Age : ")

            if ( Person_age.isdigit() ) :
                print(f"\n\n Person created with name : {Person_name} and age : {Person_age}")
                break
            else :
                print("\n Please enter the valid input !...")


        L1.append({'Person_name' : Person_name , 
                    'Person_age' : Person_age})


class Employee : 

    def Create_Employee (self) :

        global  L1

        while True :

            Employee_name = input("\n\n\tEnter the Employee Name : ")

            if ( Employee_name.isalpha() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Employee_age = input("\n\tEnter the Employee Age : ")

            if ( Employee_age.isdigit() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Employee_ID = input("\n\tEnter the Employee ID : ")

            if ( Employee_ID.isalnum() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Employee_salary = input("\n\tEnter the Employee Salary : ")

            if ( Employee_salary.isdigit() ) :
                print(f"\n\n Employee created with name : {Employee_name} , age : {Employee_salary} , ID : {Employee_ID} and salary : ${Employee_salary}")
                break
            else :
                print("\n Please enter the valid input !...")


        L1.append({'Employee_name' : Employee_name , 
                    'Employee_age' : Employee_age , 
                    'Employee_ID' : Employee_ID ,
                    'Employee_salary' : Employee_salary })


class Manager : 

    def Create_Manager (self) :

        global  L1

        while True :

            Manager_name = input("\n\n\tEnter the Manager Name : ")

            if ( Manager_name.isalpha() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Manager_age = input("\n\tEnter the Manager Age : ")

            if ( Manager_age.isdigit() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Manager_ID = input("\n\tEnter the Manager ID : ")

            if ( Manager_ID.isalnum() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Manager_department = input("\n\tEnter the Manager department : ")

            if ( Manager_department.isalpha() ) :
                break
            else :
                print("\n Please enter the valid input !...")


        while True :

            Manager_salary = input("\n\tEnter the Manager Salary : ")

            if ( Manager_salary.isdigit() ) :
                print(f"\n\n Manager created with name : {Manager_name} , age : {Manager_age} , ID : {Manager_ID} , salary : ${Manager_salary} and department : {Manager_department}")
                break
            else :
                print("\n Please enter the valid input !...")


        L1.append({'Manager_name' : Manager_name , 
                    'Manager_age' : Manager_age , 
                    'Manager_ID' : Manager_ID ,
                    'Manager_salary' : Manager_salary ,
                    'Manager_department' : Manager_department})





class Show_Information (Person , Employee , Manager) : 

    def show_information (self) :

        choice = input("""\n\n\tChoose details to show :  \n
                1. Person 
                2. Employee
                3. Manager \n
                Enter your choice : """)

        if ( choice == '1' ) :
            for i in L1 :
                if ( 'Person_name'  in  i ) :
                    print("\n Person Name :" , i['Person_name'])
                    print(" Person Age :" , i['Person_age'])

        elif ( choice == '2' ) :
            for i in L1 :
                if ( 'Employee_name'  in  i ) :
                    print("\n Employee Name :" , i['Employee_name'])
                    print(" Employee Age :" , i['Employee_age'])
                    print(" Employee ID :" , i['Employee_ID'])
                    print(" Employee Salary :" , i['Employee_salary'])

        elif ( choice == '3' ) :
            for i in L1 :
                if ( 'Manager_name'  in  i ) :
                    print("\n Manager Name :" , i['Manager_name'])
                    print(" Manager age :" , i['Manager_age'])
                    print(" Manager ID :" , i['Manager_ID'])
                    print(" Manager salary :" , i['Manager_salary'])
                    print(" Manager department :" , i['Manager_department'])

        else :
            print("\n Please enter the valid input !...")



class Call (Show_Information) :

    def menu (self) :

        while True :

            choice = input("""\n Choose an operation :  \n
        1. Create a Person 
        2. Create an Employee 
        3. Create a Manager 
        4. Show Details 
        5. Exit  \n
        Enter your choice : """)


            if ( choice == '1' ) :
                self.Create_Person()
                print("\n\n" , "*" * 100)
            elif ( choice == '2' ) :
                self.Create_Employee()
                print("\n\n" , "*" * 100)
            elif ( choice == '3' ) :
                self.Create_Manager()
                print("\n\n" , "*" * 100)
            elif ( choice == '4' ) :
                self.show_information()
                print("\n\n" , "*" * 100)
            elif ( choice == '5' ) :
                print("\n Thank you to using OOP Wrapper !...")
                break
            else :
                print("\n Please enter the valid input !...")



a = Call()
a.menu()