import shelve
from datetime import datetime


db_name = 'product'
db_product_key = 'product'


def check_status(product):
    return product.status > 0


def by_time_updated(product):
    return product.time_updated


def get_product_list():
    product_dict = {}
    db = shelve.open(db_name)
    if db_product_key in db:
        product_dict = db[db_product_key]
    db.close()
    product_list = product_dict.values()
    product_list = filter(check_status, product_list)
    product_list = sorted(product_list, key=by_time_updated, reverse=True)
    return product_list


def get_product(id):
    result = None
    product_dict = {}
    db = shelve.open(db_name)
    if db_product_key in db:
        product_dict = db[db_product_key]
    db.close()
    if id in product_dict:
        result = product_dict[id]
    return result


def save_product(product):
    product.time_updated = datetime.now()
    product_dict = {}
    db = shelve.open(db_name)
    if db_product_key in db:
        product_dict = db[db_product_key]
    product_dict[product.id] = product
    db[db_product_key] = product_dict
    db.close()
