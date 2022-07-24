from atexit import register
from django.contrib import admin
from BRMapp import models
from BRMapp.models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','price','author','publisher')

admin.site.register(Book,BookAdmin)
