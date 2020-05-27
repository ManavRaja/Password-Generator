# import modules
import string
import secrets
import random
from random import randint
import time
from art import text2art


# function for getting input as int for pwd length
def input_int(question):
    num = input(question)
    while num.isnumeric() == False:
        print("That's not an integer. You can only input an integer! Please try again.")
        num = input(question)
    return num


# ascii art
print(text2art("Password  Generator"))
time.sleep(1.5)
print(text2art("Coded  With  Python..."))
time.sleep(1.5)
print(text2art("By  @ManavRaja"))

time.sleep(1)

# getting input for pwd
print("Please input a whole number for the password's length & 'Yes' or 'No' for all the other paramaters.(Case Sensitive)")
time.sleep(3)
pwd_length = int(input_int("Password Character Length:  "))
pwd_upper = input("Should the password contain Upper Case letters?(Yes or No)  ")
pwd_lower = input("Should the password contain Lower Case letters?(Yes or No)  ")
pwd_num = input("Should the password contain Numbers?(Yes or No)  ")
pwd_spec_charac = input("Should the password contain Special Characters?(Yes or No)  ")


# generate pwd function inside eror handling
try:
    def generate_password(pwd_length, pwd_upper, pwd_lower, pwd_num, pwd_spec_charac):

        characters = ""
    
        if pwd_upper == "Yes" or "Y" or "y":
            characters = characters + string.ascii_uppercase
        if pwd_lower == "Yes" or "Y" or "y":
            characters = characters + string.ascii_lowercase
        if pwd_num == "Yes" or "Y" or "y":
            characters = characters + string.digits
        if pwd_spec_charac == "Yes" or "Y" or "y":
            characters = characters + string.punctuation
    
        password = "".join(secrets.choice(characters) for i in range(pwd_length))
        return(f"Your Strong Password is: \n{password}")


    print(generate_password(pwd_length, pwd_upper, pwd_lower, pwd_num, pwd_spec_charac))
except IndexError:
    print("You can't set all paramaters to 'No' and have it generate you a password! Please try again and set atleast 1 of the paramaters to 'Yes'.")
    while pwd_upper == pwd_lower == pwd_num == pwd_spec_charac == "No":
        pwd_upper = input("Should the password contain Upper Case letters?(Yes or No)  ")
        pwd_lower = input("Should the password contain Lower Case letters?(Yes or No)  ")
        pwd_num = input("Should the password contain Numbers?(Yes or No)  ")
        pwd_spec_charac = input("Should the password contain Special Characters?(Yes or No)  ")