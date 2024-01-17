class Customer():
    count_id = 0

    def __init__(self, first_name, last_name, email, password, gender, dob, contact_number, height, shoe_size, personal_style, events):
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password
        self.__gender = gender
        self.__dob = dob
        self.__contact_number = contact_number
        self.__height = height
        self.__shoe_size = shoe_size
        self.__personal_style = personal_style
        self.__events = events

    # Getter methods

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_gender(self):
        return self.__gender

    def get_dob(self):
        return self.__dob

    def get_contact_number(self):
        return self.__contact_number

    def get_height(self):
        return self.__height

    def get_shoe_size(self):
        return self.__shoe_size

    def get_personal_style(self):
        return self.__personal_style

    def get_events(self):
        return self.__events

    # Setter methods

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

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

    def set_height(self, height):
        self.__height = height

    def set_shoe_size(self, shoe_size):
        self.__shoe_size = shoe_size

    def set_personal_style(self, personal_style):
        self.__personal_style = personal_style

    def set_events(self, events):
        self.__events = events
