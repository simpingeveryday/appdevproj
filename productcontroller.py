import os

from flask import Blueprint, render_template, request, redirect, current_app
from productforms import CreateProductForm, UpdateProductForm
from product import Product
from productservice import get_product_list, get_product, save_product

product_controller = Blueprint('product', __name__)


@product_controller.route('/retrieveProduct')
def retrieve_products():
    product_list = get_product_list()
    return render_template('retrieveProduct.html', count=len(product_list), product_list=product_list)


@product_controller.route('/productbase')
def reksksksh():
    product_list = get_product_list()
    return render_template('productbase.html', count=len(product_list), product_list=product_list)


@product_controller.route('/createProduct', methods=['GET', 'POST'])
def create_product():
    create_product_form = CreateProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():
        name = create_product_form.name.data
        rentprice = create_product_form.rentprice.data
        stock = create_product_form.stock.data
        retailprice = create_product_form.retailprice.data
        discount = create_product_form.discount.data
        description = create_product_form.description.data
        product = Product(name, rentprice, stock, retailprice, discount, description)
        print(product)
        save_product(product)
        return redirect('/retrieveProduct')
    else:
        return render_template('createProduct.html', form=create_product_form)


@product_controller.route('/updateProduct/<id>', methods=['GET', 'POST'])
def update_product(id):
    product = get_product(id)
    update_product_form = UpdateProductForm(request.form)
    if request.method == 'POST' and update_product_form.validate():
        product.name = update_product_form.name.data
        product.rentprice = update_product_form.rentprice.data
        product.retailprice = update_product_form.retailprice.data
        product.stock = update_product_form.stock.data
        product.discount = update_product_form.discount.data
        product.description = update_product_form.description.data

        uploaded_file = request.files['image_file']
        if uploaded_file.filename != '':
                new_filename = f'{product.id}.jpg'
                uploaded_file.save(
                    os.path.join(os.path.dirname(current_app.instance_path),
                                 "static\\image", new_filename))
                product.profile_image = new_filename

        print(product)
        save_product(product)
        return redirect('/retrieveProduct')
    else:
        update_product_form.name.data = product.name
        update_product_form.retailprice.data = product.retailprice
        update_product_form.rentprice.data = product.rentprice
        update_product_form.stock.data = product.stock
        update_product_form.discount.data = product.discount
        update_product_form.description.data = product.description
        return render_template('updateProduct.html', form=update_product_form, product=product)


@product_controller.route('/deleteProduct/<id>', methods=['POST'])
def delete_product(id):
    product = get_product(id)
    product.status = product.status_deleted
    save_product(product)
    return redirect('/retrieveProduct')
