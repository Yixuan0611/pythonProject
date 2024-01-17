from flask import Flask, redirect, url_for, render_template, request, session, flash
from Forms import CreateCustomerForm, CreateProductForm, CreateStaffForm, LoginForm
import shelve, Customer, Products, Staff
from LoginCheck import logincheck

app = Flask(__name__,static_url_path='/static')
app.secret_key = 'your_secret_key'
customers_dict = {}
staff_dict = {}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    create_login_form = LoginForm(request.form)
    if request.method == 'POST' and create_login_form.validate():
        customer = logincheck(create_login_form.email.data, create_login_form.password.data)
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()
        staff_dict = {}
        db = shelve.open('staff.db', 'r')
        staff_dict = db['Staff']
        db.close()
        if customer.email_get() in customers_dict:
            user = customers_dict.get(customer.email_get())
            if customer.password_get() == request.form['password']:
                email = customer.email_get()
                return redirect(url_for('viewcustomerprofile', email=email))
            elif customer.email_get() in staff_dict:
                print('in staff db')
                user = staff_dict.get(customer.email_get())
                print(user.get_password())
                if customer.password_get() == request.form['password']:
                    email = user
                    return redirect(url_for('viewstaffprofile', email=email))
    return render_template('login.html', form=create_login_form)

@app.route('/logout')
def logout():
    session.pop('user_role', None)
    return redirect(url_for('login'))

#CRUD for customer
@app.route('/newcustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                     create_customer_form.email.data, create_customer_form.password.data,
                                     create_customer_form.gender.data, create_customer_form.dob.data,
                                     create_customer_form.contact_number.data, create_customer_form.height.data,
                                     create_customer_form.shoe_size.data, create_customer_form.personal_style.data,
                                     create_customer_form.events.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('viewcustomerprofile', id=customer.get_customer_id()))
    return render_template('create_customer.html', form=create_customer_form)

@app.route('/retrievecustomerprofiles')
def retrieve_customer():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('z_customerprofiles.html', count=len(customers_list), customers_list=customers_list)

@app.route('/customerprofile/<int:id>/')
def viewcustomerprofile(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()
    customer = customers_dict.get(id)
    return render_template('interface_customer.html', customer=customer)

@app.route('/updatecustomerprofile/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_password(update_customer_form.password.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_dob(update_customer_form.dob.data)
        customer.set_contact_number(update_customer_form.contact_number.data)
        customer.set_height(update_customer_form.height.data)
        customer.set_shoe_size(update_customer_form.shoe_size.data)
        customer.set_personal_style(update_customer_form.personal_style.data)
        customer.set_events(update_customer_form.events.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrievecustomerprofiles'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.password.data = customer.get_password()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.dob.data = customer.get_dob()
        update_customer_form.contact_number.data = customer.get_contact_number()
        update_customer_form.height.data = customer.get_height()
        update_customer_form.shoe_size.data = customer.get_shoe_size()
        update_customer_form.personal_style.data = customer.get_personal_style()
        update_customer_form.events.data = customer.get_events()

        return render_template('update_customer.html', form=update_customer_form)

@app.route('/deletecustomerprofile/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('viewcustomerprofile'))


#CRUD for staff
@app.route('/newstaff', methods=['GET', 'POST'])
def create_staff():
    create_staff_form = CreateStaffForm(request.form)
    if request.method == 'POST' and create_staff_form.validate():
        staff_dict = {}
        db = shelve.open('staff.db', 'c')

        try:
            staff_dict = db['Staff']
        except:
            print("Error in retrieving Staff from staff.db.")

        staff = Staff.Staff(create_staff_form.first_name.data, create_staff_form.last_name.data,
                            create_staff_form.email.data, create_staff_form.password.data,
                            create_staff_form.gender.data, create_staff_form.dob.data,
                            create_staff_form.contact_number.data, create_staff_form.position.data)
        staff_dict[staff.get_staff_id()] = staff
        db['Staff'] = staff_dict

        db.close()

        return redirect(url_for('viewstaffprofile', id=staff.get_staff_id()))
    return render_template('create_staff.html', form=create_staff_form)

@app.route('/retrievestaffprofiles')
def retrieve_staff():
    staff_dict = {}
    db = shelve.open('staff.db', 'r')
    staff_dict = db['Staff']
    db.close()

    staffs_list = []
    for key in staff_dict:
        staff = staff_dict.get(key)
        staffs_list.append(staff)

    return render_template('z_staffprofiles.html', count=len(staffs_list), staffs_list=staffs_list)

@app.route('/staffprofile/<int:id>')
def viewstaffprofile(id):
    staff_dict = {}
    db = shelve.open('staff.db', 'r')
    staff_dict = db['Staff']
    db.close()
    staff = staff_dict.get(id)
    return render_template('interface_staff.html', staff=staff)

@app.route('/updatestaffprofile/<int:id>/', methods=['GET', 'POST'])
def update_staff(id):
    update_staff_form = CreateStaffForm(request.form)
    if request.method == 'POST' and update_staff_form.validate():
        staff_dict = {}
        db = shelve.open('staff.db', 'w')
        staff_dict = db['Staff']

        staff = staff_dict.get(id)
        staff.set_first_name(update_staff_form.first_name.data)
        staff.set_last_name(update_staff_form.last_name.data)
        staff.set_email(update_staff_form.email.data)
        staff.set_password(update_staff_form.password.data)
        staff.set_gender(update_staff_form.gender.data)
        staff.set_dob(update_staff_form.dob.data)
        staff.set_contact_number(update_staff_form.contact_number.data)
        staff.set_position(update_staff_form.position.data)

        db['Staff'] = staff_dict
        db.close()

        return redirect(url_for('retrievestaffprofiles'))
    else:
        staff_dict = {}
        db = shelve.open('staff.db', 'r')
        staff_dict = db['Staff']
        db.close()

        staff = staff_dict.get(id)
        update_staff_form.first_name.data = staff.get_first_name()
        update_staff_form.last_name.data = staff.get_last_name()
        update_staff_form.email.data = staff.get_email()
        update_staff_form.password.data = staff.get_password()
        update_staff_form.gender.data = staff.get_gender()
        update_staff_form.dob.data = staff.dob()
        update_staff_form.contact_number.data = staff.get_contact_number()
        update_staff_form.position.data = staff.get_position()

        return render_template('update_staff.html', form=update_staff_form)

@app.route('/deletestaffprofile/<int:id>', methods=['POST'])
def delete_staff(id):
    staff_dict = {}
    db = shelve.open('staff.db', 'w')
    staff_dict.pop(id)

    db['Staff'] = staff_dict
    db.close()

    return redirect(url_for('retrievestaffprofiles'))

"""
#CRUD for products
@app.route('/create_products', methods=['GET', 'POST'])
def create_products():
    create_products_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_products_form.validate():
        products_dict = {}
        db = shelve.open('products.db', 'c')

        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Users from products.db.")

        product = Products.Products(create_products_form.name.data, create_products_form.price.data,
                                    create_products_form.quantity.data, create_products_form.description.data)
        products_dict[product.get_product_id()] = product
        db['Products'] = products_dict

        db.close()

        return redirect(url_for('retrieve_products'))
    return render_template('create_products.html', form=create_products_form)

@app.route('/retrieve_products')
def retrieve_products():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)

    return render_template('interface_cart.html', count=len(products_list), products_list=products_list)

@app.route('/update_products/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        products_dict = {}
        db = shelve.open('products.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        product.set_name(update_product_form.name.data)
        product.set_price(update_product_form.price.data)
        product.set_quantity(update_product_form.quantity.data)
        product.set_description(update_product_form.description.data)

        db['Products'] = products_dict
        db.close()

        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        db = shelve.open('products.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        update_product_form.name.data =product.get_name()
        update_product_form.price.data = product.get_price()
        update_product_form.quantity.data = product.get_quantity()
        update_product_form.description.data = product.get_description()

        return render_template('update_products.html', form=update_product_form)

@app.route('/delete_product/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    db = shelve.open('products.db', 'w')
    products_dict = db['Products']

    products_dict.pop(id)

    db['Products'] = products_dict
    db.close()

    return redirect(url_for('retrieve_products'))
"""


#app.route for bases
@app.route('/a_homepage')
def homepage():
    return render_template('a_homepage.html')

@app.route('/a_productspage')
def productspage():
    return render_template('a_productspage.html')

@app.route('/a_promotionalpage')
def promotionalpage():
    return render_template('a_promotionalpage.html')

@app.route('/z_stockdatabase')
def stockdatabase():
    return render_template('z_stockdatabase.html')


if __name__ == '__main__':
    app.run(debug=True)
