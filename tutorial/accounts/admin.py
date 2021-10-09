from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import Book
from accounts.models import OrderItem
from accounts.models import OrderDetail

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(OrderItem)
admin.site.register(OrderDetail)
