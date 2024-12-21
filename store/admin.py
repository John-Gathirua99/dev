from django.contrib import admin
from .models import Product,Category,Customer,Orders
# Register your models here.


admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Category)
admin.site.register(Customer)
