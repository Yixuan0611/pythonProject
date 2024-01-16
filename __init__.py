from flask import Flask, redirect, url_for, render_template, request, session, flash
from Forms import CreateCustomerForm, CreateProductForm, CreateStaffForm, LoginForm
import shelve, Customer, Products, Staff

app = Flask(__name__,static_url_path='/static')
app.secret_key = 'your_secret_key'
customers_dict = {}
staff_dict = {}

@app.route('/')
def home():
    if 'user_role' in session:
        if session['user_role'] == 'staff':
            return render_template('interface_staff.html')
        elif session['user_role'] == 'customer':
            # Assuming customer_profile contains the customer's profile information
            customer_profile = viewprofile(id)
            return render_template('interface_customer.html', customer_profile=customer_profile)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    create_login_form = LoginForm(request.form)
    if request.method == 'POST' and create_login_form.validate():
        customer_dict = {}
        db = shelve.open('customer.db', 'r')
        customer_dict = db['Customers']
        db.close()
        staff_dict = {}
        db = shelve.open('staff.db', 'r')
        staff_dict = db['Staff']
        db.close()

        email = create_login_form.email.data
        password = create_login_form.password.data

        if email in customer_dict:
            user = customer_dict[email]
            if password == user.get_password():
                user_role = 'customer'
                return redirect(url_for('interface_customer'))
        elif email in staff_dict:
            user = staff_dict[email]
            if password == user.get_password():
                user_role = 'staff'
                return redirect(url_for('interface_staff'))

    return render_template('login.html', form=create_login_form)


@app.route('/logout')
def logout():
    session.pop('user_role', None)
    return redirect(url_for('login'))

#CRUD for customer
@app.route('/create_customer', methods=['GET', 'POST'])
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
                            create_customer_form.gender.data, create_customer_form.email.data, create_customer_form.dob.data,
                            create_customer_form.height.data, create_customer_form.shoe_size.data,
                            create_customer_form.personal_style.data, create_customer_form.events.data,
                            create_customer_form.points.data, create_customer_form.password.data)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('viewprofile', id=customer.get_customer_id()))
    return render_template('create_customer.html', form=create_customer_form)

@app.route('/z_customerprofiles')
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

@app.route('/interface_customer/<int:id>')
def viewprofile(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()
    customer = customers_dict.get(id)
    return render_template('interface_customer.html', customer=customer)

@app.route('/update_customer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_dob(update_customer_form.dob.data)
        customer.set_height(update_customer_form.height.data)
        customer.set_shoe_size(update_customer_form.shoe_size.data)
        customer.set_personal_style(update_customer_form.personal_style.data)
        customer.set_events(update_customer_form.events.data)
        customer.set_points(update_customer_form.points.data)
        customer.set_password(update_customer_form.password.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customer'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.dob.data = customer.get_dob()
        update_customer_form.height.data = customer.get_height()
        update_customer_form.shoe_size.data = customer.get_shoe_size()
        update_customer_form.personal_style.data = customer.get_personal_style()
        update_customer_form.events.data = customer.get_events()
        update_customer_form.points.data = customer.get_points()
        update_customer_form.password.data = customer.get_password()

        return render_template('update_customer.html', form=update_customer_form)

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customer'))

#CRUD for products
@app.route('/createProducts', methods=['GET', 'POST'])
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

        return redirect(url_for('interface_cart'))
    return render_template('create_products.html', form=create_products_form)


@app.route('/retrieveProducts')
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

@app.route('/updateProducts/<int:id>/', methods=['GET', 'POST'])
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

@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    db = shelve.open('products.db', 'w')
    products_dict = db['Products']

    products_dict.pop(id)

    db['Products'] = products_dict
    db.close()

    return redirect(url_for('retrieve_products'))



#app.route for bases
@app.route('/a_homepage')
@app.route('/viewprofile/a_homepage')
def homepage():
    return render_template('a_homepage.html')

@app.route('/a_productspage')
@app.route('/viewprofile/a_productspage')
def productspage():
    return render_template('a_productspage.html')

@app.route('/a_promotionalpage')
@app.route('/viewprofile/a_promotionalpage')
def promotionalpage():
    return render_template('a_promotionalpage.html')

@app.route('/z_customerprofiles')
def customerprofiles():
    return render_template('z_customerprofiles.html')

@app.route('/z_staffprofiles')
def staffprofiles():
    return render_template('z_staffprofiles.html')

@app.route('/z_stockdatabase')
def stockdatabase():
    return render_template('z_stockdatabase.html')



if __name__ == '__main__':
    app.run(debug=True)
