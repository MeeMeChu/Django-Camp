from django.contrib import admin
from app_students.models import Division, StudentInfo , FavoriteSub

# Register your models here.
@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','psu_id', 'division_set' ,'date']
    search_fields = ['psu_id']
    list_filter = ['division_set']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ['name', ]

@admin.register(FavoriteSub)
class FavoriteSubAdmin(admin.ModelAdmin):
    list_display = ['name', ]