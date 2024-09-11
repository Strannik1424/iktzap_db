from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.IntegerField(unique=True)  # Уникальное поле для фильтрации
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
   
    def __str__(self):
        return f'{self.category_id} - {self.title}'