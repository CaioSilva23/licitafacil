from django.contrib import admin
from clientes.models import Cliente, EmailContato, Newslatter

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email', 'telefone', 'servico')
    list_per_page = 20
    search_fields = ('nome', 'email', 'servico')
    readonly_fields = ('nome','sobrenome','email', 'telefone', 'servico')
admin.site.register(Cliente, ClienteAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_per_page = 20
    search_fields = ('email',)
    readonly_fields = ('email',)
admin.site.register(Newslatter, NewsAdmin)    


class EmailContatoAdmin(admin.ModelAdmin):
    list_display = ('email','assunto')
    list_per_page = 20
    search_fields = ('email','assunto')
    readonly_fields = ('email','assunto', 'texto')
admin.site.register(EmailContato, EmailContatoAdmin)