import re
import hashlib


class Account:

    num_of_acc = 0

# cant we take first and last name and create username out of those?

#    def __init__(self, first_name, last_name, password, phone_no, email) -> None:
#
#        Account.num_of_acc += 1
#        self.username = first_name+"_"+last_name
#        self.password = password
#        self.phone_no = phone_no
#        self.email = email

    def __init__(self, username, password, phone_no, email) -> None:

        Account.num_of_acc += 1
        self.username = username
        self.password = self.check_password(password)
        self.phone = self.check_phone(phone_no)
        self.email = email

    @staticmethod
    def check_username(username):

        if not re.search("^\w+_\w+$", username):
            raise Exception('invalid username')
        return username

    @staticmethod
    def check_password(password):

        def check_password(cls, password):
            if not all([re.search("[a-z]", password), re.search("[A-Z]", password), len(password) > 7]):
                raise Exception('invalid password')
        encoded = password.encode('utf-8')
        return hashlib.sha256(encoded)

    @staticmethod
    def check_phone_no(phone_no):

        if not (re.search("^((\+989)|(09))+[0-3,9]\d{8}$", phone_no)):
            raise Exception('invalid phone number')
        return phone_no

    @staticmethod
    def check_email(email):

        if not re.search("([A-Za-z0-9]+[.-_])+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,5})+", email):
            raise Exception('invalid email')
        return email


class Site:
#inja tu paraanteze init benevisam 2 ta variable ke user meghdar nemide?

    def __init__(self, url):
        self.url = url
        self.registered_users = []
        self.active_users = []

    def register(self):
        pass

    def login(self):
        pass
#ina chi migiran? az classe balayi username ro mifahman?

    def logout(self, username):
        pass


account1 = Account('ali','jamali',"Aa123123" ,2)
print(account1.username)
