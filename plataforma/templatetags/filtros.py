from django import template

register = template.Library()


@register.filter(name='formata_preco')
def formata_preco(value):
    return f'R$ {value:.2f}'.replace('.',',')