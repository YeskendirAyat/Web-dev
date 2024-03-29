from django.db import models
'''
# create table core_product(
#     id INTEGER ,
#     name VARCHAR(255),
#     price NUMBER DEFAULT = 0,
#     description VARCHAR(500),
#     count INTEGER ,
# );
'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'description':self.description,
            'count':self.count,
            'is_active':self.is_active
        }
class Category(models.Model):
    name = models.CharField(max_length=255)
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name
        }