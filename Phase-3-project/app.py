from db.setup import init_db
from cli import (display_menu, create_user, delete_user, display_all_users, find_user_by_username,
                 create_password_entry, delete_password_entry, display_all_password_entries,
                 find_password_entry_by_id, view_all_password_entries_for_user)

def main():
    init_db()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            find_user_by_username()
        elif choice == '5':
            create_password_entry()
        elif choice == '6':
            delete_password_entry()
        elif choice == '7':
            display_all_password_entries()
        elif choice == '8':
            find_password_entry_by_id()
        elif choice == '9':
            view_all_password_entries_for_user()
        elif choice == '0':
            print("Exiting Password Manager CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
