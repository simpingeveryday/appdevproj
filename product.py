import uuid
from datetime import datetime
from constants import datetime_format


class Product:
    status_active = 1
    status_deleted = 0

    def __init__(self, name, retailprice, rentprice, stock, discount, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.retailprice = retailprice
        self.rentprice = rentprice
        self.stock = stock
        self.discount = discount
        self.description = description
        self.status = Product.status_active
        self.time_created = datetime.now()
        self.time_updated = datetime.now()
        self.profile_image = None

    # #def get_name(self):
    #     return self.name
    #
    # def get_retailprice(self):
    #     return self.retailprice
    #
    # def get_rentprice(self):
    #     return self.rentprice
    #
    # def get_stock(self):
    #     return self.stock
    #
    # def get_discount(self):
    #     return self.discount
    #
    # def get_d6escription(self):
    #     return self.description

    def get_time_created_str(self):
        return self.time_created.strftime(datetime_format)

    def get_time_updated_str(self):
        return self.time_updated.strftime(datetime_format)

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Name: {self.name}\n' \
               f'Retail Price: {self.retailprice}\n' \
               f'Rent Price: {self.rentprice}\n' \
               f'Stock: {self.stock}\n' \
               f'Discount: {self.discount}\n' \
               f'Description: {self.description}\n' \
               f'Status: {self.status}\n' \
               f'Date Created: {self.get_time_created_str()}\n' \
               f'Date Updated: {self.get_time_updated_str()}\n'
