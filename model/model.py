__author__ = 'ISP-PC'

from google.appengine.ext import ndb

class TeamDB(ndb.Model):
        firstname = ndb.StringProperty(default='empty')
        lastname = ndb.StringProperty(default='empty')
        email = ndb.StringProperty()
        idno = ndb.IntegerProperty(default=0)
        phone = ndb.StringProperty(default='empty')
        hiredate = ndb.StringProperty(default='empty')
        job = ndb.StringProperty(default='empty')
        type = ndb.StringProperty(default='empty')
        privilege = ndb.StringProperty(default='user')



class ProductDB(ndb.Model):
        quantity = ndb.IntegerProperty(default=10)
        category = ndb.StringProperty()
        date = ndb.DateProperty(auto_now_add=True)
        supplier= ndb.StringProperty(default='none')
        status = ndb.StringProperty(default='active')
        price = ndb.IntegerProperty(default=0)
        image_link = ndb.StringProperty()

class SupplierDB(ndb.Model):
        business_name = ndb.StringProperty()
        phone = ndb.StringProperty()
        email = ndb.StringProperty()
        county = ndb.StringProperty()
        town = ndb.StringProperty()

class OrderDB(ndb.Model):
        quantity = ndb.IntegerProperty()
        supplier = ndb.IntegerProperty()
        item = ndb.IntegerProperty()
        customer = ndb.IntegerProperty()

