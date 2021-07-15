from django.db import models

# Create your models here.
# class Tag(models.Model):
#     tags = models.CharField(max_length=100,null = False, blank =False)
#     def __str__(self):
#         return self.tags

class Categorise(models.Model):
    name = models.CharField(max_length=100,null = False, blank =False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    # tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Categorise, on_delete=models.CASCADE)
    image= models.ImageField(upload_to = 'photo', null =False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date']

    
