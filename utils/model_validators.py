from PIL import Image
from django.db.models import ImageField
from django.core.exceptions import ValidationError

def validate_img(image:ImageField):
    imagem = image.image
    imagem_pil = Image.open(imagem.path)

    max_area = 89478485

    width = imagem_pil.width
    height = imagem_pil.height
    area = width * height

    image_name = image.name.lower()
    
    if not image_name.endswith('.jpg') or image_name.endswith('.png'):
        raise ValidationError('Coloque apenas imagens em .PNG ou .JPG')

    if area > max_area:
        raise ValidationError('A imagem excede o limite de tamanho.')

