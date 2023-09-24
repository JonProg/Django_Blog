# Generated by Django 4.2.2 on 2023-09-22 17:36

from django.db import migrations, models
import utils.model_validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postattachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='posts/%Y/%m/', validators=[utils.model_validators.validate_img]),
        ),
    ]
