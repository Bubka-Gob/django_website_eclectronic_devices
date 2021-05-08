from django import template

register = template.Library()

@register.filter
def model_to_user(str):
    return str.replace('User model', 'Пользователь')