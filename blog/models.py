from django.db import models
from utils.rands import slugify_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        unique = True, default = None,
        null = True, blank = True, max_length = 150
    )

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        super().save(*args, **kwargs)



class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
    
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        unique = True, default = None,
        null = True, blank = True, max_length = 150
    )

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        super().save(*args, **kwargs)
