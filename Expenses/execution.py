from userDBoperations import insert_user, view_users, search_user
from categoryDBoperations import insert_category, view_category
from ExpensesDBoperation import add_expenses, search_expenses_by_user_and_category

def menu():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. User Management")
        print("2. Category Management")
        print("3. Expense Management")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # ---------- USER ----------
        if choice == "1":

            while True:

                print("\n----- USER MANAGEMENT -----")
                print("1. Insert User")
                print("2. View Users")
                print("3. Search User")
                print("4. Back")

                option = input("Enter your choice: ")

                if option == "1":
                    insert_user()

                elif option == "2":
                    view_users()

                elif option == "3":
                    search_user()

                elif option == "4":
                    break

                else:
                    print("Invalid Choice!")

        # ---------- CATEGORY ----------
        elif choice == "2":

            while True:

                print("\n----- CATEGORY MANAGEMENT -----")
                print("1. Insert Category")
                print("2. View Category")
                print("3. Back")

                option = input("Enter your choice: ")

                if option == "1":
                    insert_category()

                elif option == "2":
                    view_category()

                elif option == "3":
                    break

                else:
                    print("Invalid Choice!")

        # ---------- EXPENSE ----------
        elif choice == "3":

            while True:

                print("\n----- EXPENSE MANAGEMENT -----")
                print("1. Add Expense")
                print("2. Search Expense")
                print("3. Back")

                option = input("Enter your choice: ")

                if option == "1":
                    add_expenses()

                elif option == "2":
                    search_expenses_by_user_and_category()

                elif option == "3":
                    break

                else:
                    print("Invalid Choice!")

        # ---------- EXIT ----------
        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    # create_tables()
    menu()