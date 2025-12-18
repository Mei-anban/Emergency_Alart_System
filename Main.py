from Emergency_alart import add_contect,view_contect,delete_all,delete_contect
from Alart_triger import send_alart
from Logging import log_alart,send_email,view_alarts


def menu():
    
    while True:
        print("\n=== Emergency Alert System ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Delete All Contacts")
        print("5. Send Emergency Alert")
        print("6. View Alert Logs")
        print("7. Exit")

        choice = int(input("Enter your choise: "))

        if choice == 1 :
            name = input("Enter name : ")
            phone = input("Enter phone : ")
            email = input("Enter Email : ")
            relation = input("Enter relation : ")
            add_contect(name,phone,email,relation)

        elif choice == 2 :
            view_contect()

        elif choice == 3 :
            contect_id = int(input("Enter contect id to delete : "))
            delete_contect(contect_id)

        elif choice == 4 :
            delete_all()

        elif choice == 5 :
            subject = input("Enter the subject : ")
            message = input("Enter alart message : ")
            send_alart(subject,message)

        elif choice == 6 :
            view_contect()

        elif choice == 7 :
            print("Exiting system....")
            break

        else:
            print("Invaild Choice, Try again.")

menu()

