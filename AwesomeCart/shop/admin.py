# from itertools import product
from django.contrib import admin
from .models import Product, Orders, Contact, OrderUpdate

# Register your models here.
'''
pip install windows-curses // In case getting error in  migrations
'''
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Contact)
admin.site.register(OrderUpdate)