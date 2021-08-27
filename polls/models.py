from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    Gender =[
        ('M', 'Male'),
        ('F ','Female'),
        ] 
    artist_gender = models.CharField(max_length=2, choices=Gender, null=True)
    
    def __str__(self):
        return self.name
    

class Album(models.Model):
    name = models.CharField(max_length=100)
    no_of_songs = models.IntegerField()
    trailer_date = models.DateField()
    out_date = models.DateField()
    no_of_artist = models.IntegerField()
  
    def __str__(self):
        return self.name 



    
class Song(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='singer' ,on_delete= models.CASCADE, related_query_name='singers', null=True)
    artist =models.ManyToManyField(Artist)
    no_of_artist = models.IntegerField()
    out_date = models.DateField()
 
  
    
    def __str__(self):
        return self.name
    

class lyrics(models.Model):
    name = models.CharField(max_length=100)
    songs = models.OneToOneField(Song, on_delete=models.CASCADE, related_query_name='singers')
  
class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
   
    

    

    
    
    
    
  
        
        
    
