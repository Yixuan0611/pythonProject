from Customer import Customer
from Staff import Staff
class logincheck:
    def __init__(self, email2, password2):
        Customer.count_id += 1
        self.__email2 = email2
        self.__password2 = password2

    def logincheckfunc(self):
        print("it means its works!!!!! you hear that yishun~~!!!!!!!! bob")

    def logincheckfunc2(self):
        print("it means its works!!!!! you hear that yishun~~!!!!!!!! bob22222222")
    def email_get(self):
        return self.__email2

    def password_get(self):
        return self.__password2

    def email_set(self,email):
        self.__email2 = email
    def password_set(self,password):
        self.__password2 = password