def who_do_you_know():
    user_answer = input("enter the names of all those whom you know, sepaared by commas\nYour answer : ")
    return user_answer.split(',')

def ask_user():
    user_answer = input('Please enter your first name\nYour answer : ')
    if user_answer in name_list:
        print('You are known')
    else:
        print('You are not known')

name_list=who_do_you_know()
ask_user()
