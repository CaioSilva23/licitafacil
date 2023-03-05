from django.contrib import admin
from plataforma.models import Secao1, Secao2, Servicos, Secao3, Secao4, Secao5
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Servicos)

# SEÇÃO HOME DA EMPRESA
class Secao1Admin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao1.objects.exists()
admin.site.register(Secao1, Secao1Admin)


# SEÇÃO SERVIÇOS DA EMPRESA
class Secao2Admin(SummernoteModelAdmin):
    summernote_fields = ['saiba_mais']

    def has_add_permission(self, *args, **kwargs) -> bool:
        return len(Secao2.objects.all()) < 3
admin.site.register(Secao2, Secao2Admin)


# SEÇÃO SOBRE O DIFERENCIAL DA EMPRESA
class Secao3Admin(SummernoteModelAdmin):
    summernote_fields = ['paragrafo']
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao3.objects.exists()
admin.site.register(Secao3, Secao3Admin)


# SEÇÃO CONTATOS DA EMPRESA
class ContatoAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao4.objects.exists()
admin.site.register(Secao4, ContatoAdmin)


# SEÇÃO SOBRE O DIFERENCIAL DA EMPRESA
class Secao5Admin(SummernoteModelAdmin):
    summernote_fields = ['paragrafo']
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao5.objects.exists()
admin.site.register(Secao5, Secao5Admin)
