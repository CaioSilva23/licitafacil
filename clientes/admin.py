from django.contrib import admin
from . models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email', 'telefone', 'servico')
    list_per_page = 20
    search_fields = ('nome', 'email', 'servico')

admin.site.register(Cliente, ClienteAdmin)