from wtforms import Form, StringField, IntegerField, SelectField, TextAreaField, validators, DecimalField, PasswordField, RadioField
from wtforms.fields import EmailField, DateField


class LoginForm(Form):
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=5, max=15), validators.DataRequired()])



class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=150), validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    dob = DateField('Date of Birth', [validators.DataRequired()], format='%Y-%m-%d')
    contact_number = StringField('Contact Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    height = IntegerField('Height', [validators.NumberRange(min=90), validators.Optional()])
    shoe_size = IntegerField('Shoe Size', [validators.NumberRange(min=1), validators.Optional()])
    personal_style = StringField('Personal Style', [validators.Length(max=150), validators.Optional()])
    events = StringField('Events', [validators.Optional()])  # Assuming events is a string that contains event data

class CreateStaffForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=150), validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=5, max=15), validators.data_required()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    dob = DateField('Date of Birth', [validators.DataRequired()], format='%Y-%m-%d')
    contact_number = StringField('Contact Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    position = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')


class CreateProductForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    price = DecimalField('Price', [validators.NumberRange(min=0), validators.DataRequired()])
    quantity = IntegerField('Quantity', [validators.NumberRange(min=0), validators.DataRequired()])
    description = TextAreaField('Description', [validators.Optional(), validators.Length(max=1024)])
    category = SelectField('Category', [validators.DataRequired()], choices=[])  # Choices need to be populated dynamically


