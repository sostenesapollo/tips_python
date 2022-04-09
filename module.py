while True:
    username = input("Username:")
    password = input("Password:")

    if username == 'admin' and password == 'admin':
        break
    
    print("Wrong username or password !")