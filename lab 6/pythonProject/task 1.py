class UserAccount:
    def __init__(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self,new_password):
        self.password = new_password
    def check_password(self,password_to_check):
        return self.password == password_to_check

user = UserAccount(input('Name '),input('email '),input('password '))

new=input('Do you want to set new password? \n 1 - yes \n 2 - no \n')
if new == 1:
    new_password = input('Enter new password ')
    user.set_password(new_password)


while True:
    password_to_verify = input('Enter password to verify: ')
    if user.check_password(password_to_verify):
        print('Password is correct')
        break
    else:
        print('Password is incorrect')



