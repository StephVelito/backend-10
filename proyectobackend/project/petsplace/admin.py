from django.contrib import admin
from .models import CitasModel, CategoriasModel, ClientesModel

# Register your models here.
class ShowDetails(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'estado')

admin.site.register(CitasModel, ShowDetails)
admin.site.register(CategoriasModel)
admin.site.register(ClientesModel)

