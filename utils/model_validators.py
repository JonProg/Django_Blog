from django.core.exceptions import ValidationError

def validate_img(image:str):
    if image.name.lower().endswith('.png'):
        raise ValidationError('Coloque apenas imagens em .PNG')
