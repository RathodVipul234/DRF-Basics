from django.db import models

# Create your models here.
gender = (
    ('Male', "Male"),
    ('Female', "Female")
)


class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=gender, max_length=10)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
