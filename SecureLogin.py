#Diego Osornio
#12/4/2024



valid_username = "Duck"
valid_password = "Balls"



def login():
    # Hardcoded valid username and password (modify these)
    valid_username = "Duck"
    valid_password = "Balls"

    # Get user input for username and password
x= input("What is your username? : ")
y= input("What is your password? : ")
    # Convert the entered username to lowercase or uppercase by using a method for case-insensitive comparison
x = x.lower()
y = y.lower()
    # Check if the entered username and password match the valid credentials
if x == valid_username:
    print("Your username is NOT registered")
else:
    print("Your username is registered")

if x == valid_password:
    print("Your password is NOT correct")

else:
     print("Your password is correct")
     print("welcome")


# Call the function to check credentials
login()
