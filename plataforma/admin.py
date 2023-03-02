from django.contrib import admin
from plataforma.models import Plataforma
from plataforma.models import Secao1, Secao2, Card, Servicos, Secao4


admin.site.register(Servicos)

class Secao1Admin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao1.objects.exists()
admin.site.register(Secao1, Secao1Admin)


class CardInline(admin.TabularInline):
    # list_display = ('nome', 'quantidade', 'descricao')
    #readonly_fields = ('nome', 'quantidade', 'descricao')
    model = Card
    extra = 0

class Secao2Admin(admin.ModelAdmin):
    inlines = [CardInline]
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao2.objects.exists()
admin.site.register(Secao2, Secao2Admin)


class PlataformaAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Plataforma.objects.exists()
admin.site.register(Plataforma, PlataformaAdmin)


class ContatoAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs) -> bool:
        return not Secao4.objects.exists()
admin.site.register(Secao4, ContatoAdmin)