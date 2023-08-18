from django.contrib import admin
from .models import Books,Avtors
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','book_name')
    search_fields = ['book_name','id']

class AvtorsAdmin(admin.ModelAdmin):
        search_fields = ['avtor_name', 'id']
admin.site.register(Books,BooksAdmin)
admin.site.register(Avtors,AvtorsAdmin)