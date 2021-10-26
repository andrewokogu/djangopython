from django.contrib import admin
from .models import Book, Student

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Student)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'no_of_pages', 'isbn', 'date']
    list_editable = ['isbn']
    list_filter = ['date']
    list_per_page = 2
    search_fields = ['title', 'body','author']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'department', 'course','date_of_entry']
    list_editable = ['department']
    list_filter = ['course']
    list_per_page = 2
    search_fields = ['name', 'department','course']    