from django.contrib import admin
from .models import User
# Register your models here.

class userAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    

admin.site.register(User,userAdmin)
