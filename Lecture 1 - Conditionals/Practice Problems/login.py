# Write a function login(username, password) that takes two strings username and password.
# If the username is "admin" and the password is "password123", print "Access Granted".
# Otherwise, print "Access Denied".

def main():
    username = input("Enter your username: ")
    password = input("Enter yout password: ")
    login(username, password)

def login(name, pw):
    if name == "admin" and pw == "password123":
        print("Access Granted")
    else:
        print("Access Denied")

if __name__ == "__main__":
    main()