class Staff():
    count_id = 0

    def __init__(self, first_name, last_name, email, password, gender, dob, contact_number, position):
        Staff.count_id += 1
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__dob = dob
        self.__contact_number = contact_number
        self.__staff_id = Staff.count_id
        self.__position = position

    # Getter methods

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

    def get_staff_id(self):
        return self.__staff_id

    def get_position(self):
        return self.__position


    # Setter methods

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

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_position(self, position):
        self.__position = position
