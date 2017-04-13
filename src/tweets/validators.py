from django.core.exceptions import ValidationError

def no_abc(value):
    content = value
    if content == "abc":
        raise ValidationError("Content cannot be abc")

    return content
