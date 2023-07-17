import datetime as date

# User sign up function
def SignUp():
    print("Please enter your Username by which you want to access this diary.")
    username = input("Input here:  ")
    print("Create a passcode to secure this diary.")
    password = input("Input here:  ")

    user_information(username,password)
    print("Your sign up is complete! Proceed to login... ")
    login()

# Storing user information function
def user_information(usrnm, pswrd):
    print("Thank you for signing up! We just need some more information to set up your diary!")
    name = input("What is your name?   ")
    age = input("How old are you?   ")
    usrnm_ = usrnm + " Diary.txt"

    with open(usrnm_, 'a') as f:
        f.write(pswrd+'\n')
        f.write("\nNAME\n")
        f.write(name+"\n")
        f.write("AGE\n")
        f.write(age+"\n\n")

# User login function
def login():
    print("Enter your username and password")
    user_nm = input("Enter your Username here:   ")
    psswd_ = (input("Enter your Password here:   ")) + '\n'

    try:
        usrnm = user_nm + " Diary.txt"
        with open(usrnm, 'r') as f_:
            password = f_.readline().strip()  # Reading the first line which is the password.

            if psswd_.strip() == password:
                print("Welcome " + user_nm)
            else:
                print("YOUR PASSWORD OR USERNAME IS WRONG, TRY AGAIN")
                login()
    except Exception as e:
        print(e)
        login()

if __name__ == '__main__':
    print("WELCOME TO YOUR DIARY!")
    while True:
        a = int(input("Type 1 and hit Enter if you're new, otherwise type 0 and hit Enter for login: "))
        if a == 1:
            SignUp()
            break
        elif a == 0:
            login()
            break
        else:
            print("WRONG INPUT! Try again: ")
