from django.db import models

# Create your models here.
class categories(models.Model):
    title = models.CharField(max_length=100)
    description =models.TextField()
    no_of_vacancy = models.IntegerField()
    images = models.ImageField(upload_to = 'jobimages')

    def __str__(self):
        return self.title


class jobs(models.Model):
    title = models.CharField(max_length=30)
    description =models.TextField()
    no_of_vacancy = models.IntegerField()
    images = models.ImageField(upload_to = 'jobimages')
    experience = models.TextField()
    documents =models.TextField()
    skills = models.TextField()
    language = models.TextField()
    salary = models.TextField()
    age = models.TextField()
    cat = models.ForeignKey('categories',on_delete=models.CASCADE,related_name='jobs')

    def __str__(self):
        return self.title