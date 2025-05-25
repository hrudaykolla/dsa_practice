# def MainDoor():
#     print("you have entered my Home")

# #Task wrap the MainDoor with a lock

# def LockForDoor(passcode, door): #decorator
#     def passCodeVerification(): #wrapper
#         if passcode == 1234:
#             print("Access Granted")
#             return door()
#         else:
#             print("Access Denied")
#     return passCodeVerification() #return the wrapper

# LockForDoor(1234, MainDoor)
# print(MainDoor.__name__)

# #----------------------------------
from functools import wraps
def LockForDoor(door):
    @wraps(door)
    def passCodeVerification(passcode):
        if passcode == 1234:
            print("Access Granted")
            return door()
        else:
            print("Access Denied")
    return passCodeVerification

@LockForDoor
def MainDoor():
    print("You have entered my Home")

# Using the decorated MainDoor function
MainDoor(1234) # This will now prompt for passcode verification and print the result

print(MainDoor.__name__)
# wrapper function comes as the output instead of the fucntion. it overrode the name
#functools.wraps
#once i use @wraps, the maindoor remains maindoor

