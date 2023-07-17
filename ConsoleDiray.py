import os
import getpass
import bcrypt
import datetime as date

class User:
    def __init__(self, username, password, name=None, age=None):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.file_path = f"{self.username}_diary.txt"

    def verify_password(self, password_attempt):
        with open(self.file_path, 'r') as f:
            stored_password = f.readline().strip()
        return bcrypt.checkpw(password_attempt.encode(), stored_password.encode())
        

    def save(self):
        # Hash the password before saving it
        hashed_password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode()

        with open(self.file_path, 'a') as f:
            f.write("----------------------------------------------------\n")
            f.write(f"PASSWORD HASH\n{hashed_password}\n")
            f.write("----------------------------------------------------\n")
            f.write(f"NAME\n{self.name}\n")
            f.write(f"AGE\n{self.age}\n")
            f.write("----------------------------------------------------\n\n")

    def add_entry(self):
        print("\n-------------Write your diary entry below:-------------\n")
        entry = input()
        with open(self.file_path, 'a') as f:
            f.write(f"DATE: {date.datetime.now()}\n")
            f.write("----------------------------------------------------\n")
            f.write("ENTRY:\n")
            f.write(entry + "\n")
            f.write("----------------------------------------------------\n\n")
        print("\nYour entry has been saved!\n")

class Diary:
    @staticmethod
    def signup():
        print("\n--------------- New User Sign Up ---------------")
        username = input("Please enter your Username by which you want to access this diary:  ")
        password = getpass.getpass("Create a passcode to secure this diary:  ")
        name = input("What is your name?:   ")
        age = input("How old are you?:   ")

        user = User(username, password, name, age)
        user.save()
        print("\nYour sign up is complete! Proceed to login... ")
        Diary.login()

    @staticmethod
    def login():
        print("\n--------------- User Login ---------------")
        username = input("Enter your Username here:   ")
        password = getpass.getpass("Enter your Password here:    ")

        user_file = f"{username}_diary.txt"

        if not os.path.exists(user_file):
            print("User does not exist. Try again or sign up")
            return
        user = User(username, password)
        if user.verify_password(password):
            print(f"\nWelcome {username}\n")
            while True:
                print("Type 1 and hit Enter to add a new entry, or type 0 and hit Enter to quit: ")
                action = input()
                if action == "1":
                    user.add_entry()
                elif action == "0":
                    print("\nExiting the diary...\n")
                    break
                else:
                    print("Invalid input! Please type 1 to add an entry or 0 to quit.")
        else:
            print("YOUR PASSWORD OR USERNAME IS WRONG, TRY AGAIN")
            Diary.login()

if __name__ == '__main__':
    print("\n\n--------------- WELCOME TO YOUR DIARY ---------------")
    while True:
        try:
            action = int(input("\nType 1 and hit Enter if you're new, otherwise type 0 and hit Enter for login: "))
            if action == 1:
                Diary.signup()
                break
            elif action == 0:
                Diary.login()
                break
            else:
                print("WRONG INPUT! Please type 0 for login or 1 for sign up")
        except ValueError:
            print("Invalid input! Please type 0 for login or 1 for sign up.")
