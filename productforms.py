# Note: Use wtforms v3.0.0
from wtforms import Form, StringField, TextAreaField, \
    validators, FloatField, IntegerField


class CreateProductForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    rentprice = FloatField('Rent Price', [validators.DataRequired()])
    retailprice = FloatField('Retail Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])


class UpdateProductForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    rentprice = FloatField('Rent Price', [validators.DataRequired()])
    retailprice = FloatField('Retail Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
