#ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is valid and False if it's not.
def ATM(pin):
    if len(pin) == 4 or len(pin) == 6 and pin.isdigit():
        return True
    else:
        return False
print(ATM("1234"))
