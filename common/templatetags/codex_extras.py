from django import template

register = template.Library()

@register.filter(name='runeify')
def runeify(value):
    if value is None:
        return ''
    text = str(value).strip()
    if not text:
        return ''
    return f"† {text} †"