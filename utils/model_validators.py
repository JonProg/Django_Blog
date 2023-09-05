from django.db.models import ImageField
from django.core.exceptions import ValidationError

def validate_img(image:ImageField):
    max_area = 89478485

    width = image.width
    height = image.height
    area = width * height

    image_name = image.name.lower()
    
    if not image_name.endswith('.jpg') or image_name.endswith('.png'):
        raise ValidationError('Coloque apenas imagens em .PNG ou .JPG')

    if area > max_area:
        raise ValidationError('A imagem excede o limite de tamanho.')

