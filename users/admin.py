from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustumUserAdmin(UserAdmin):
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost",)
    pass


"""
위 데코레이터를 쏜 코드는 아래 코드와 같은 뜻이다  

class CustumUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.User , CustumUserAdmin)

"""
