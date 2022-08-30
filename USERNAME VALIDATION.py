user_name=input("enter the user name:")

re_enter_username=input("re enter the user name:")
if list(user_name) == list(re_enter_username):
    print("username is correct")
else:
    print("invalid username")
