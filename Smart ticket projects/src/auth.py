def login():
    print("=== SmartTicket AI Login ===")
    user = input("Username: ")
    password = input("Password: ")
    # Hardcoded for simplicity/demo
    if user == "admin" and password == "admin123":
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Credentials.\n")
        return False
