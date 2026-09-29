userid = "admin"
passwaord = "1234"

i = 1

while i <=3:
    user = input("Enter User ID: ")
    pwd = input("enter Password: ")

    if user == userid and pwd == passwaord:
        print("Login Successful")
        break
    else:
        print("Invalid User ID or Password")

    i = i +1    