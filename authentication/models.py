from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
             
class Departament(models.Model):
    name = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=10, blank=True, null=True)
    id_country = models.ForeignKey("Country", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

class City(models.Model):
    id_department = models.ForeignKey("Departament", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abreviation = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    id_city = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
