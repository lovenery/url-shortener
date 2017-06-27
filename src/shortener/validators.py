from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()

    if "http" in value:
        new_value = value
    else:
        new_value = "http://" + value

    try:
        url_validator(new_value)
    except:
        raise ValidationError('Invalid URL for this field')

    return new_value

def validate_dot_com(value):
    if not "." in value:
        raise ValidationError("NO . DOT in url")
    return value