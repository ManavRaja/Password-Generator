import string
import secrets
import random
from random import randint


def input_int(question):
    num = input(question)
    while num.isnumeric() == False:
        print("Thats's not an integer. You can only input an integer! Please try again.")
        num = input(question)
    return num


pwd_min_length = int(input_int("Password Minimum Length:  "))
pwd_max_length = int(input_int("Password Maximum Length:  "))


class GeneratePassword:

    def generate_password(self, pwd_min_length, pwd_max_length):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        number_between_min_max = randint(pwd_min_length, pwd_max_length)
        password = "".join(secrets.choice(alphabet) for i in range(number_between_min_max))
        return(f"Your Strong Passwprd is: \n{password}")


pwd = GeneratePassword()
print(pwd.generate_password(pwd_min_length, pwd_max_length))