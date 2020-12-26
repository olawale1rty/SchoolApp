from django.contrib import admin
from .models import Profile,Workshop, RegisterWorkshopUser

admin.site.register(Profile)
admin.site.register(Workshop)

class RegisterWorkshopUserAdmin(admin.ModelAdmin):
	list_filter = ['workshop']

admin.site.register(RegisterWorkshopUser, RegisterWorkshopUserAdmin)