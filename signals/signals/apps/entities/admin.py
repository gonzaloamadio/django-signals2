from django.contrib import admin

from . import models

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'create_at','update_at')

@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'create_at', 'update_at')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

