from django.db import models

class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_color = models.CharField(max_length=255)
    p_time = models.DateTimeField(auto_now_add=True)
    p_image = models.ImageField(upload_to='pics')
    p_content = models.TextField()
    def __str__(self):
        return self.p_content
