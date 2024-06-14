from models.user import User
from models.password_entry import PasswordEntry
from db.setup import get_session
from utils.validators import validate_username, validate_password, validate_email

def display_menu():
    print("\nPassword Manager CLI")
    print("1. Create User")
    print("2. Delete User")
    print("3. Display All Users")
    print("4. Find User by Username")
    print("5. Create Password Entry")
    print("6. Delete Password Entry")
    print("7. Display All Password Entries")
    print("8. Find Password Entry by ID")
    print("9. View All Password Entries for a User")
    print("0. Exit")

def create_user():
    try:
        username = input("Enter username: ")
        validate_username(username)
        password = input("Enter password: ")
        validate_password(password)
        email = input("Enter email: ")
        validate_email(email)

        with get_session() as session:
            user = User.create(session, username, password, email)
            print(f"Created user: {user}")
    except ValueError as e:
        print(f"Error: {e}")

def delete_user():
    try:
        user_id = int(input("Enter user ID to delete: "))
        with get_session() as session:
            User.delete(session, user_id)
            print(f"Deleted user with ID: {user_id}")
    except ValueError:
        print("Invalid input. Please enter a valid user ID.")

def display_all_users():
    with get_session() as session:
        users = User.get_all(session)
        for user in users:
            print(user)

def find_user_by_username():
    username = input("Enter username to find: ")
    with get_session() as session:
        user = User.find_by_username(session, username)
        if user:
            print(user)
        else:
            print(f"No user found with username: {username}")

def create_password_entry():
    try:
        site_name = input("Enter site name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = int(input("Enter user ID: "))

        with get_session() as session:
            entry = PasswordEntry.create(session, site_name, username, password, user_id)
            print(f"Created password entry: {entry}")
    except ValueError:
        print("Invalid input. Please ensure all fields are correctly filled.")

def delete_password_entry():
    try:
        entry_id = int(input("Enter password entry ID to delete: "))
        with get_session() as session:
            PasswordEntry.delete(session, entry_id)
            print(f"Deleted password entry with ID: {entry_id}")
    except ValueError:
        print("Invalid input. Please enter a valid entry ID.")

def display_all_password_entries():
    with get_session() as session:
        entries = PasswordEntry.get_all(session)
        for entry in entries:
            print(entry)

def find_password_entry_by_id():
    try:
        entry_id = int(input("Enter password entry ID to find: "))
        with get_session() as session:
            entry = PasswordEntry.find_by_id(session, entry_id)
            if entry:
                print(entry)
            else:
                print(f"No password entry found with ID: {entry_id}")
    except ValueError:
        print("Invalid input. Please enter a valid entry ID.")

def view_all_password_entries_for_user():
    try:
        user_id = int(input("Enter user ID to view password entries: "))
        with get_session() as session:
            user = User.find_by_id(session, user_id)
            if user:
                for entry in user.password_entries:
                    print(entry)
            else:
                print(f"No user found with ID: {user_id}")
    except ValueError:
        print("Invalid input. Please enter a valid user ID.")
