from django.db import models
# Create your models here.


class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('description')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'LIST'
        verbose_name_plural = 'INFORMATION'