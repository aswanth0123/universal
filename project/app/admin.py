from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(product)
admin.site.register(weight)
admin.site.register(users)
admin.site.register(addreses)
admin.site.register(contacts)
admin.site.register(cart_item)
admin.site.register(orders)
admin.site.register(reviews)