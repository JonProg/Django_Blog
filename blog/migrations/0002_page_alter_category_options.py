# Generated by Django 4.2.2 on 2023-06-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('slug', models.SlugField(blank=True, default='', max_length=255, unique=True)),
                ('is_published', models.BooleanField(default=False, help_text='Este campo precisará estar marcado para a página ser exibida publicamente.')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
