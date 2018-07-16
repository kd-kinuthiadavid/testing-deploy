from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    '''
    Location model
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class category(models.Model):
    '''
    Category model
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
       return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()



class Image(models.Model):
    '''
    Image model
    '''
    image = models.ImageField(upload_to='gallery/')
    image_url = models.TextField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    category = models.ManyToManyField(category)
    post_date = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location)

    def __str__(self):
       return self.name

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def get_painting(cls, category):
        image = cls.objects.get(category=5)
        return image

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(description__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls, id):
        images = cls.objects.filter(location_id=id)
        return images
