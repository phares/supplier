#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2,jinja2,os
from model.model import ProductDB,OrderDB,SupplierDB,TeamDB


template_path = os.path.join(os.path.dirname(__file__))

jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_path))

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))

class BackHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/backend.html')
        self.response.out.write(template.render(template_values))


def new_order(quantity, customer, supplier, item):
    pass
    order =OrderDB(
        quantity = quantity,
        customer = customer,
        supplier = supplier,
        item = item
    )
    order.put()


class OrderHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/order.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        quantity = self.request.get("")
        customer = self.request.get("")
        supplier = self.request.get("")
        item = self.request.get("")

        new_order(quantity,customer,supplier,item)


def new_product(quantity, category, supplier, status, price, image_link):
    pass
    product = ProductDB(

            quantity = int(quantity),
            category = category,
            supplier = supplier,
            status = status,
            price = int(price),
            image_link = image_link

        )

    product.put()


class ProductHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/product.html')
        self.response.out.write(template.render(template_values))

    def post(self):

        quantity = self.request.get("quantity")
        category = self.request.get("category")
        supplier = self.request.get("supplier")
        status = self.request.get("status")
        price = self.request.get("price")
        image_link = self.request.get("image_link")

        new_product(quantity,category,supplier,status,price,image_link)


def new_supplier(business_name, phone, email, county, town):
    pass
    supplier = SupplierDB(
        business_name = business_name,
        phone = phone,
        email = email,
        county = county,
        town = town
    )
    supplier.put()


class SupplierHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/supplier.html')
        self.response.out.write(template.render(template_values))

    def post(self):

        business_name = self.request.get("business_name")
        phone = self.request.get("phone")
        email = self.request.get("email")
        county = self.request.get("county")
        town = self.request.get("town")

        new_supplier(business_name,phone,email,county,town)


def new_team_member(firstname, lastname, email, idno, phone, hiredate, job, type, privilege):
    pass
    member = TeamDB(
        firstname = firstname,
        lastname =lastname,
        email = email,
        idno = idno,
        phone = phone,
        hiredate = hiredate,
        job = job,
        type = type,
        privilege = privilege
    )
    member.put()


class TeamHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/team.html')
        self.response.out.write(template.render(template_values))

    def post(self):

        firstname = self.request.get("")
        lastname = self.request.get("")
        email = self.request.get("")
        idno = self.request.get("")
        phone = self.request.get("")
        hiredate = self.request.get("")
        job = self.request.get("")
        type = self.request.get("")
        privilege = self.request.get("")

        new_team_member(firstname,lastname,email,idno,phone,hiredate,job,type,privilege)


class ProductDetailsHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/product-details.html')
        self.response.out.write(template.render(template_values))

class ProductsHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/shop.html')
        self.response.out.write(template.render(template_values))

class CheckOutHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/checkout.html')
        self.response.out.write(template.render(template_values))

class CartHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/cart.html')
        self.response.out.write(template.render(template_values))

class LoginHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/login.html')
        self.response.out.write(template.render(template_values))

class ShippingAddressHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/shipping-address.html')
        self.response.out.write(template.render(template_values))

class BlogHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/blog.html')
        self.response.out.write(template.render(template_values))

class BlogSingleHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/blog-single.html')
        self.response.out.write(template.render(template_values))

class Error404Handler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/404.html')
        self.response.out.write(template.render(template_values))

class ContactUsHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/contact-us.html')
        self.response.out.write(template.render(template_values))

class ShoppersHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/shoppers.html')
        self.response.out.write(template.render(template_values))

class SkeletonHandler(webapp2.RequestHandler):
    def get(self):

        template_values = {

        }

        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/skeleton.html')
        self.response.out.write(template.render(template_values))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/backend', BackHandler),
    ('/order', OrderHandler),
    ('/product', ProductHandler),
    ('/supplier', SupplierHandler),
    ('/team', TeamHandler),
    ('/products', ProductsHandler),
    ('/shoppers', ShoppersHandler),
    ('/shipping_address', ShippingAddressHandler),
    ('/checkout', CheckOutHandler),
    ('/product_details', ProductDetailsHandler),
    ('/cart', CartHandler),
    ('/login', LoginHandler),
    ('/blog', BlogHandler),
    ('/blog_single', BlogSingleHandler),
    ('/404', Error404Handler),
    ('/contact_us', ContactUsHandler),
    ('/skeleton', SkeletonHandler),
], debug=True)
