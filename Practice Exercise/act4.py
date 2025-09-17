#Relational & Boolean Operators
username = "joshua_fronda"
password = "secure123"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if input_username == username and input_password == password:
    print("Access granted.")
else:
    print("Access denied.")
