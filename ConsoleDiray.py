import datetime as date

def SignUp():
    print("Please enter your Username by which you wanna access this diary")
    username = input("Input here:  ")
    print("Create a passcode to secure this diary")
    password = input("Input here:  ")

    user_information(username,password)
    print("Your sign up is complete! Proceed to login... ")
    login()

def user_information(usrnm,pswrd):
    print("Thank you for signing up! We just need some more information to set up your diary!")
    name = input("What is your name?   ")
    age = input("How old are you?   ")
    usrnm_ = usrnm+" Diary.txt"

    f = open(usrnm_, 'a')
    f.write(pswrd)
    f.write("\nNAME\n")
    f.write(name+"\n")
    f.write("AGE\n")
    f.write(age+"\n\n")
    f.close()

def login():
    print("Enter your username and password")
    user_nm = input("Enter your Username here:   ")
    psswd_ = (input("Enter your Password here:   ")) + '\n'

    try:
        usrnm = user_nm+" Diary.txt"
        f_ = open(usrnm, 'r')
        k_ = f_.readline(0)[0]
        f_.close()

        if psswd_ == k_:
            print("Welcome "+user_nm)
        else:
            print("YOUR PASSSWORD OR USERNAME IS WRONG, TRY AGAIN")
            login()
    except Exception as e:
        print(e)
        login()

if __name__ == '___main___':
    print("WELCOME TO YOUR DIARY!")
    a = int(input("Type 1 and hit Enter if you're new, otherwise type 0 and hit Enter for login"))
    if a == 1:
        SignUp()
    elif a == 0:
        login()
    else:
        print("WRONG INPUT! Try again: ")