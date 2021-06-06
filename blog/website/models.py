from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length= 2,
        choices= Categorias.choices,
        default= Categorias.GR, 
    )

    approved = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def title_subtitle(self):
        return self.title + ' - ' + self.sub_title
    
    title_subtitle.admin_order_field = 'title'

