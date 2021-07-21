from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps
import re
from db_orm import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'ecommercebahartara'


def create_token(email, access):
    token = jwt.encode(
        {'email': email, 'access': access, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=4)},
        app.config['SECRET_KEY'], algorithm="HS256")
    return token


def validate_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
        return False
    return True


def authentication(function):
    @wraps(function)
    def token_and_login(*args, **kwargs):
        headers = request.headers
        authorizarion_header = headers.get('Authorization')
        if authorizarion_header:
            try:
                token = authorizarion_header.split(" ")[1]
            except:
                return jsonify({'authorization': 'Failed', 'message': 'Malformed Authorization header'}), 401
            authorized = validate_token(token)
            if authorized:
                return function(*args, **kwargs)
            else:
                return jsonify({'authorization': 'Failed', 'message': 'Invalid token'}), 401

    return token_and_login


@app.route('/login', methods=['POST'])
@db_session
def login():
    body = request.get_json()
    email = body.get('email')
    password = body.get('password')
    user = select(user for user in User if user.email == email)[:]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.match(regex, email)):
        if len(user) != 0:
            user = user[0]
            if user.password == password:
                created_token = create_token(email, user.admin)
                return jsonify({'token': created_token,'name':user.name, 'message':'ورود با موفقیت انجام شد'})
            else:
                return jsonify({'authorization': 'Failed', 'message': 'wrong password'}), 403

        else:
            return jsonify({'authorization': 'Failed', 'message': 'user does not exist'}), 403
    else:
        return jsonify({'authorization': 'Failed', 'message': 'Malformed email'}), 403


@app.route('/signup', methods=['POST'])
@db_session
def signup():

    body = request.get_json()
    email = body.get('email')
    password = body.get('password')
    emailregex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    passwordregex = '(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,255})$'
    if email == None and password == None:
        return jsonify({'message': 'email and password not provided'}), 400

    elif password == None and email != None:
        return jsonify({'message': 'password was not provided'}), 400

    elif password != None and email == None:
        return jsonify({'message': 'email was not provided'}), 400

    else:
        if re.match(emailregex, email):
            if re.match(passwordregex, password):
                user = select(user for user in User if user.email == email)[:]
                if len(user) != 0:
                    return jsonify({'message': 'user already exists'}), 400
                else:
                    address = body.get('address')
                    name = body.get('name')
                    sname = body.get('sname')
                    if address != None:
                        if len(address) > 1000:
                            return jsonify({'message': 'address too long'}), 400
                    elif name != None:
                        if len(name) > 250:
                            return jsonify({'message': 'name too long'}), 400
                    elif sname != None:
                        if len(sname) > 250:
                            return jsonify({'message': 'surname too long'}), 400

                    User(email=email, password=password, admin=0, name=body.get('name'), sname=body.get('sname'),
                         address=body.get('address'))
                    created_token = create_token(email, 0)
                    return jsonify({'token': created_token, 'message':'ثبت‌ نام با موفقیت انجام شد'})

            else:
                return jsonify({
                                   'message': 'the password must contain both letters and numbers and be at least 8 characters long'}), 400

        else:
            return jsonify({'message': 'invalid email address'}), 400


@app.route('/products', methods=['GET'])
@db_session
def getProducts():
    order = request.args.get("order")
    if order == 'priceDesc':
        products = select(p for p in Product).order_by(desc(Product.price))

    elif order == 'priceAsc':
        products = select(p for p in Product).order_by(Product.price)


    elif order == 'sold':
        products = select(p for p in Product).order_by(desc(Product.sold))

    elif order=='date':
        products = select(p for p in Product).order_by(desc(Product.date))

    # products = select(p for p in Product).order_by(desc(Product.sold))
    prods = []
    for product in products:
        prods.append({'title': product.name, 'date': product.date, 'price': product.price, 'sold': product.sold,
                      'category': product.category, 'available': product.available})



    return jsonify(prods)


@app.route('/filtercat', methods=['POST'])
@db_session
def categoryFilter():
    order = request.args.get("order")
    body = request.get_json()
    categories = body.get("cats")
    if order == 'priceDesc':
            products = select(p for p in Product if p.category in categories).order_by(desc(Product.price))

    elif order == 'priceAsc':
        products = select(p for p in Product if p.category in categories).order_by(Product.price)


    elif order == 'sold':
        products = select(p for p in Product if p.category in categories).order_by(desc(Product.sold))

    elif order=='date':
        products = select(p for p in Product if p.category in categories).order_by(desc(Product.date))

    # products = select(p for p in Product).order_by(desc(Product.sold))
    prods = []
    for product in products:
        prods.append({'title': product.name, 'date': product.date, 'price': product.price, 'sold': product.sold,
                      'category': product.category, 'available': product.available})



    return jsonify(prods)


@app.route('/categories', methods=['GET'])
@db_session
def getcats():
    categories = select(c for c in Category)
    cats = []
    for cat in categories:
        cats.append(cat.name)
    return jsonify(cats)

@app.route('/searchproduct', methods=['GET'])
@db_session
def searchProduct():

    productName =  request.args.get("product")
    if productName == "":
        getProducts()
    product = select(p for p in Product if p.name == productName)[:]

    prods = []
    if len(product)!=0:
        product = select(p for p in Product if p.name == productName)[:][0]
        prods.append({'title': product.name, 'date': product.date, 'price': product.price, 'sold': product.sold,
                          'category': product.category, 'available': product.available})

    return jsonify(prods)


@app.route('/buy', methods=['POST'])
@authentication
@db_session
def buy():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    body = request.get_json()
    product = body.get('product')
    num = int(body.get('number'))
    content_type = headers.get('content-type')
    email = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get('email')
    user = select(user for user in User if user.email == email)[:][0]
    product = select(p for p in Product if p.name == product)[:][0]
    invoicePrice = num * product.price
    if invoicePrice <= user.balance:
        if num <= product.available:
            user.balance -= invoicePrice
            product.available -= num
            product.sold += num
            newInvoice = Invoice(product=product, number=num, customerName=user.name, customerSName=user.sname,
                                 address=user.address,
                                 price=invoicePrice, date=datetime.datetime.utcnow(), user=user)
            # test it later
            user.invoices.add(newInvoice)
            return jsonify({'message': 'خرید با موفقیت انجام شد'})
        else:
            return jsonify({'message': 'تعداد درخواست شده بیشتر از موجودی انبار است'}),403

    else:
        return jsonify({'message': 'موجودی ناکافی'}),403


@app.route('/balance', methods=['GET'])
@authentication
@db_session
def increaseBalance():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    email = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get('email')
    user = select(user for user in User if user.email == email)[:][0]
    user.balance += 100000
    return jsonify({'message': 'balance increased successfully', 'balance':user.balance})


@app.route('/getbalance', methods=['GET'])
@authentication
@db_session
def returnBalance():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    email = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get('email')
    user = select(user for user in User if user.email == email)[:][0]
    return jsonify({'balance': user.balance})


@app.route('/invoiceuser', methods=['GET'])
@authentication
@db_session
def invoiceUser():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    email = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get('email')
    user = select(user for user in User if user.email == email)[:][0]
    invoices = select(inv for inv in Invoice if inv.user == user)
    invs = []
    for invoice in invoices:
        invs.append({'product': invoice.product.name, 'date': invoice.date, 'price': invoice.price, 'id': invoice.id,
                     'address': invoice.address})

    return jsonify(invs)



@app.route('/invoiceadmin', methods=['GET'])
@authentication
@db_session
def invoiceAdmin():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    access = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get(
        'access')
    if access:
        invoices = select(inv for inv in Invoice)
        invs = []
        for invoice in invoices:
            invs.append(
                {'product': invoice.product.name, 'date': invoice.date, 'price': invoice.price, 'id': invoice.id,
                 'address': invoice.address,
                 'name': invoice.customerName + ' ' + invoice.customerSName})

        return jsonify(invs)
    else:
        return jsonify({'message': 'access denied'}), 403

@app.route('/idfilter', methods=['GET'])
@authentication
@db_session
def idFilter():
    headers = request.headers
    id = request.args.get('id')
    authorizarion_header = headers.get('Authorization')
    access = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get(
        'access')
    if access:
        invoice = select(inv for inv in Invoice if inv.id==id)[:]
        invs =[]
        if len(invoice)!=0:
            invoice = select(inv for inv in Invoice if inv.id == id)[:][0]
            invs.append({'product': invoice.product.name, 'date': invoice.date, 'price': invoice.price, 'id': invoice.id,
                 'address': invoice.address,
                 'name': invoice.customerName + ' ' + invoice.customerSName})
        return jsonify(invs)
    else:
        return jsonify({'message': 'access denied'}), 403

@app.route('/editprofile', methods=['POST'])
@authentication
@db_session
def editProfile():
    passwordregex = '(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,255})$'
    headers = request.headers
    body = request.get_json()
    authorizarion_header = headers.get('Authorization')
    email = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get('email')
    user = select(user for user in User if user.email == email)[:][0]

    if  body.get('name'):
        if len(body.get('name')) <= 250:
            user.name = body.get('name')

        else:
            return jsonify({'message': 'name too long'}), 400


    if  body.get('sname'):
        if len(body.get('sname')) <= 250:
            user.sname = body.get('sname')
        else:
            return jsonify({'message': 'surname too long'}), 400
    if  body.get('address'):
        if len(body.get('address')) < 1001:
            user.address = body.get('address')
            # return jsonify({'message': user.sname, 'd': user.address})
        else:
            return jsonify({'message': 'address too long'}), 400

    if  body.get('password'):
        if len(body.get('password')) <= 250 and re.match(passwordregex, body.get('password')):
            user.password = body.get('password')
            # return jsonify({'message': user.sname, 'd': user.password})
        else:
            return jsonify({'message': 'Invalid new password'}), 400

    return jsonify({'message': 'profile edited successfully'})


@app.route('/editcategory', methods=['POST'])
@authentication
@db_session
def editCat():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    access = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get(
        'access')
    if access:
        body = request.get_json()
        cat = body.get('category')
        newName = body.get('newName')
        category = select(cate for cate in Category if cate.name == cat)[:][0]
        category.name = newName
        products = select(pro for pro in Product if pro.category == cat)[:]
        for product in products:
            product.category = newName

        return jsonify({'message': 'ویرایش مورد نظر با موفقیت انجام شد'})

    else:
        return jsonify({'message': 'access denied'}), 403


@app.route('/deletecategory', methods=['POST'])
@authentication
@db_session
def deleteCat():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    access = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get(
        'access')
    if access:
        body = request.get_json()
        cat = body.get('category')
        delete(cate for cate in Category if cate.name == cat)
        products = select(pro for pro in Product if pro.category == cat)[:]
        for product in products:
            product.category = 'دسته بندی نشده'

        return jsonify({'message': 'دسته بندی مورد نظر با موفقیت حذف شد'})

    else:
        return jsonify({'message': 'access denied'}), 403


@app.route('/editproduct', methods=['POST'])
@authentication
@db_session
def editProduct():
    headers = request.headers
    authorizarion_header = headers.get('Authorization')
    access = jwt.decode(authorizarion_header.split(' ')[1], app.config['SECRET_KEY'], algorithms=["HS256"]).get(
        'access')
    if access:
        body = request.get_json()
        name = body.get('name')
        product = Product.get(name=name)
        if  body.get('newName'):
            product.name = body.get('newName')

        if  body.get('available'):
            product.available += int(body.get('available'))

        if  body.get('category'):
            cats = select(cat for cat in Category if cat.name == body.get('category'))[:]
            if not len(cats):
                Category(name=body.get('category'))
            product.category = body.get('category')

        if  body.get('price'):
            product.price = int(body.get('price'))

        return jsonify({'message': 'ویرایش مورد نظر با موفقیت انجام شد'})

    else:
        return jsonify({'message': 'access denied'}), 403


app.run()
