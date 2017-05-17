from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class AboutMe(models.Model):
    name = models.CharField(max_length=220,)
    surname = models.CharField(max_length=220,)
    street = models.CharField(max_length=220,)
    city = models.CharField(max_length=220,)
    phone = models.CharField(max_length=220,)
    github = models.CharField(max_length=220,)
    facebook = models.CharField(max_length=220,)
    description = models.TextField()
    email = models. EmailField(max_length=254,)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return str(self.name + self.surname )
    def __unicode__(self):
        return str(self.name)

class Knowledge(models.Model):
    technology = models.CharField(max_length=220,)
    description = models.TextField()
    icon = models.CharField(max_length=220,)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return str(self.technology )
    def __unicode__(self):
        return str(self.technology)



class Contact(models.Model):
    imie  = models.CharField(max_length=220,)
    nazwisko  = models.CharField(max_length=220,)
    miasto  = models.CharField(max_length=220,)
    telefon  = models.CharField(max_length=220,)
    email  = models.CharField(max_length=220,)
    github  = models.CharField(max_length=220,)
    facebook  = models.CharField(max_length=220,)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.imie )
    def __unicode__(self):
        return str(self.imie)