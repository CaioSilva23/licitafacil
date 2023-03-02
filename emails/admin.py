from django.contrib import admin
from .models import Newslatter, EmailContato
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_per_page = 20
    search_fields = ('email',)
    readonly_fields = ('email',)
    
class EmailContatoAdmin(admin.ModelAdmin):
    list_display = ('email','assunto')
    list_per_page = 20
    search_fields = ('email','assunto')
    readonly_fields = ('email','assunto', 'texto')



admin.site.register(Newslatter, NewsAdmin)
admin.site.register(EmailContato, EmailContatoAdmin)


