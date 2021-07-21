from dotenv import load_dotenv, find_dotenv
from os import getenv
import datetime
from pony.orm import *



load_dotenv(find_dotenv())

db_config = {
    "host": getenv("DB_HOST"),
    "user": getenv("DB_USER"),
    "passwd": getenv("DB_PASS"),
    "db": getenv("DB_NAME"),
}

db = Database()




class Category(db.Entity):
    id =  PrimaryKey(int, auto=True)
    name =  Required(str,255)


class Invoice(db.Entity):
    id = PrimaryKey(int, auto=True)
    product = Required('Product')
    number = Required(int)
    customerName = Required(str,255)
    customerSName = Required(str,255)
    address = Required(str,255)
    price = Required(int)
    date = Required(datetime.datetime)
    status = Optional(str,255)
    user = Required('User')

class User(db.Entity):
    email = PrimaryKey(str)
    password = Required(str,255)
    name = Optional(str,255)
    sname = Optional(str,255)
    address = Optional(str, 255)
    balance =Optional(int,default = 0)
    admin = Required(bool, default = 0)
    invoices = Set(Invoice)

class Product(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str,255)
    price = Required(int)
    available = Required(int)
    category = Required(str,255,default='دسته بندی نشده')
    sold= Required(int)
    invoices = Set(Invoice)
    date= Required(datetime.datetime)


db.bind(provider='mysql', **db_config)
db.generate_mapping(create_tables=True)


with db_session:
    if User.select().first() is None:
        User(email = 'admin@gmail.com', password= 'adminadmin1', admin=True, name='admin')
    if Category.select().first() is None:
        Category(name= 'دسته بندی نشده')
        Category(name='موس کامپیوتر')
        Category(name='ساعت')
        Category(name='عطر')
    if Product.select().first() is None:
        Product(name="موس کامپیوتر ۱", price=200000, available = 40, sold=10, category = 'موس کامپیوتر', date=datetime.datetime.utcnow())
        Product(name="موس کامپیوتر ۲", price=400000, available=20, sold=5, category = 'موس کامپیوتر'  , date=datetime.datetime.utcnow())
        Product(name="موس کامپیوتر ۳", price=100000, available=40, sold=20,  category = 'موس کامپیوتر' , date=datetime.datetime.utcnow())
        Product(name="موس کامپیوتر ۴", price=200000, available=4, sold=30,  category = 'موس کامپیوتر' , date=datetime.datetime.utcnow())
        Product(name="موس کامپیوتر ۵", price=300000, available=40, sold=0,  category = 'موس کامپیوتر' , date=datetime.datetime.utcnow())
        Product(name="ساعت ۱", price=200000, available = 40, sold=10, category = 'ساعت', date=datetime.datetime.utcnow())
        Product(name="ساعت ۲", price=400000, available=20, sold=5, category = 'ساعت'  , date=datetime.datetime.utcnow())
        Product(name="ساعت ۳", price=100000, available=40, sold=20,  category = 'ساعت' , date=datetime.datetime.utcnow())
        Product(name="ساعت ۴", price=200000, available=4, sold=30,  category = 'ساعت' , date=datetime.datetime.utcnow())
        Product(name="ساعت ۵", price=300000, available=40, sold=0,  category = 'ساعت' , date=datetime.datetime.utcnow())
        Product(name="عطر ۱", price=200000, available = 40, sold=10, category = 'عطر', date=datetime.datetime.utcnow())
        Product(name="عطر ۲", price=400000, available=20, sold=5, category = 'عطر'  , date=datetime.datetime.utcnow())
        Product(name="عطر ۳", price=100000, available=40, sold=20,  category = 'عطر' , date=datetime.datetime.utcnow())
        Product(name="عطر ۴", price=200000, available=4, sold=30,  category = 'عطر' , date=datetime.datetime.utcnow())
        Product(name="عطر ۵", price=300000, available=40, sold=0,  category = 'عطر' , date=datetime.datetime.utcnow())
        Product(name="گل", price=200000, available = 40, sold=10, category = 'دسته بندی نشده', date=datetime.datetime.utcnow())
        Product(name="خودکار", price=400000, available=20, sold=5, category = 'دسته بندی نشده'  , date=datetime.datetime.utcnow())
        Product(name="مداد", price=100000, available=40, sold=20,  category = 'دسته بندی نشده' , date=datetime.datetime.utcnow())
        Product(name="پاک کن", price=200000, available=4, sold=30,  category = 'دسته بندی نشده' , date=datetime.datetime.utcnow())
        Product(name="قلم", price=300000, available=40, sold=0,  category = 'دسته بندی نشده' , date=datetime.datetime.utcnow())
