from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a movie genre")

    def __str__(self):
        return self.name

class Thumbnail(models.Model):
    thumb_1=models.ImageField(upload_to="thumbnail")
    thumb_2=models.ImageField(upload_to="thumbnail")
    thumb_3=models.ImageField(upload_to="thumbnail")
    thumb_4=models.ImageField(upload_to="thumbnail")

class Movie(models.Model):
    resolution_choice=(
        ("1080p","1080p"),
        ("720p","720p"),
        ("480p","480p"),
    )
    movie_name=models.CharField(max_length=100)
    movie_poster=models.ImageField(upload_to="movie")
    cast=models.CharField(max_length=200)
    date_added=models.DateField(auto_now=True)
    imbd_rating=models.CharField(max_length=20)
    resolution=models.CharField(choices=resolution_choice,max_length=50)
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this movie")
    thumbnail=models.OneToOneField(Thumbnail,on_delete=models.CASCADE)
    Link_download=models.CharField(max_length=500)

    def __str__(self):
        return self.movie_name