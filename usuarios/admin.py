from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Resumo, User

# Register your models here.
admin.site.register(User, auth_admin.UserAdmin)
admin.site.register(Resumo)
