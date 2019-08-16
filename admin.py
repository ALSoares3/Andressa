from django.contrib import admin
from livros.models import Biblioteca
# Register your models here.

class AdminBiblioteca(admin.ModelAdmin):
    list_display = ( 'nome' ,)
    list_filter = ( 'nome' ,)

admin.site.register(Biblioteca, AdminBiblioteca)