from flask import Flask, request, jsonify, make_response
import jwt
import datetime
from functools import wraps
import re
from db_orm import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecommercebahartara'

def create_token(email, access):
    token = jwt.encode(
        {'email': email, 'access': access, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
        app.config['SECRET_KEY'], algorithm="HS256")
    return token

def validate_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
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
    user = select(user for user in User if user.email==email)[:]
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.match(regex, email)):
        if len(user)!=0:
            user = user[0]
            if user.password == password:
                created_token = create_token(email, user.admin)
                return jsonify({'token': created_token})
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
    if email == None and password==None:
        return jsonify({'message': 'email and password not provided'}), 400

    elif password == None and email!=None:
        return jsonify({'message': 'password was not provided'}), 400

    elif password != None and email==None:
        return jsonify({'message': 'email was not provided'}), 400

    else:
        if re.match(emailregex, email):
            if re.match(passwordregex, password):
                user = select(user for user in User if user.email == email)[:]
                if len(user)!=0:
                    return jsonify({'message': 'user already exists'}), 400
                else:
                    address = body.get('address')
                    name = body.get('name')
                    sname = body.get('sname')
                    if address!=None:
                        if len(address)>1000:
                            return jsonify({'message': 'address too long'}), 400
                    elif name!=None:
                        if len(name)>250:
                            return jsonify({'message': 'name too long'}), 400
                    elif sname!=None:
                        if len(sname)>250:
                            return jsonify({'message': 'surname too long'}), 400

                    User(email=email, password=password, admin =0, name=body.get('name'), sname=body.get('sname'),address=body.get('address'))
                    created_token = create_token(email, 0)
                    return jsonify({'token': created_token})

            else:
                return jsonify({'message': 'the password must contain both letters and numbers and be at least 8 characters long'}), 400

        else:
            return jsonify({'message': 'invalid email address'}), 400



@app.route('/products', methods=['GET'])
@db_session
def getProducts():
    body = request.get_json()
    order = body.get('order')
    if order=='price':
        products = select(p for p in Product).order_by(desc(Product.price))

    elif order == 'sold':
        products = select(p for p in Product).order_by(desc(Product.sold) )

    prods =[]
    for product in products:
        prods.append({'name':product.name, 'price':product.price, 'category':product.category, 'available':product.available})

    return jsonify(prods)


@app.route('/categories', methods=['GET'])
@db_session
def getcats():
    categories = select(c for c in Category )
    cats =[]
    for cat in categories:
        cats.append({'name':cat.name})
    return jsonify(cats)



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
    invoicePrice =  num * product.price
    if invoicePrice <= user.balance:
        if num <= product.available:
            user.balance -= invoicePrice
            product.available-= num
            product.sold +=num
            Invoice(product=product, number=num, customerName=user.name, customerSName = user.sname, address=user.address,
                 price=invoicePrice, date=datetime.datetime.utcnow())
            return jsonify({'message': 'purchase successful'})
        else:
            return jsonify({'message': 'purchase unsuccessful, product not available'})

    else:
        return jsonify({'message': 'purchase unsuccessful, balance not enough'})


app.run()