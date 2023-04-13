from django.contrib import admin

from .models import Admission, Company, UserCompany

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'image',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class UserCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'company',
    )
    search_fields = ('user', 'company')
    empty_value_display = '-пусто-'


class AdmissionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'passport',
        'number',
        'company',
    )
    search_fields = (
        'name',
        'passport',
        'number',
        'company',
    )
    empty_value_display = '-пусто-'


admin.site.register(Admission, AdmissionsAdmin)
admin.site.register(UserCompany, UserCompanyAdmin)
admin.site.register(Company, CompanyAdmin)
