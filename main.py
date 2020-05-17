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
pwd_spec_charac = input("Should the password contain special characters?(Yes or No)  ")


def generate_password(pwd_min_length, pwd_max_length, pwd_spec_charac):
    alphabet = string.ascii_letters + string.digits
    if pwd_spec_charac == "Yes":
        alphabet = alphabet + string.punctuation
    number_between_min_max = randint(pwd_min_length, pwd_max_length)
    password = "".join(secrets.choice(alphabet) for i in range(number_between_min_max))
    return(f"Your Strong Passwprd is: \n{password}")


print(generate_password(pwd_min_length, pwd_max_length, pwd_spec_charac))