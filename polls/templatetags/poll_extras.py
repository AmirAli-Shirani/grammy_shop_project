from django import template

register = template.Library()


@register.filter(name='three_digits_currency')
def persian_intcomma(value):
    str_value = str(value)[::-1]
    new_value = ''
    for i in range(len(str_value)):
        new_value += str_value[i]
        if (i + 1) % 3 == 0 and i != len(str_value) - 1:
            new_value += ','
    return new_value[::-1] + ' تومان '


@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return persian_intcomma(quantity * price)
