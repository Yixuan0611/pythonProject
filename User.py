class User:
    count_id = 0

    def __init__(self, first_name, last_name, email, password, gender, dob, contact_number):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__dob = dob
        self.__contact_number = contact_number

    # Getter methods

    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return  self.__password

    def get_gender(self):
        return self.__gender

    def get_dob(self):
        return self.__dob
    def get_contact_number(self):
        return self.__contact_number



    # Setter methods

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_gender(self, gender):
        self.__gender = gender

    def set_dob(self, dob):
        self.__dob = dob

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number


