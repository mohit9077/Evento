from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(UserReg)
admin.site.register(AdminReg)
admin.site.register(login_user)
admin.site.register(login_admin)