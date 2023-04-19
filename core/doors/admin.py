from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(DoorType)
admin.site.register(Door)
admin.site.register(News)
admin.site.register(Message)