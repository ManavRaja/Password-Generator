import string
import secrets
import random


def input_int(question):
    num = input(question)
    while num.isnumeric() == False:
        print("That's not an integer. You can only input an integer! Please try again.")
        num = input(question)
    return num


num = input_int("What should the character length of the password be?  ")


class GeneratePassword:
    def __init__(self, pwd_length=15):
        self.pwd_length = pwd_length

    def generate_pwd(self, pwd_length=15):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(int(pwd_length)))
        return(f"Your Strong Password is: \n{password}")


pwd = GeneratePassword()
print(pwd.generate_pwd(int(num)))