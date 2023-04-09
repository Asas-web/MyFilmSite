from django.db import models

class UserrManeger(models.Manager):
    def basic_validator(self,post_data):
        errors={}
        if len(post_data['firstname'])<2:
            errors['firstname']="firstname must be more than 2 charectes"
        if len(post_data['lastname'])<2:
            errors['lastname']="lastname must be more than 2 charectes"
        if len(post_data['password'])<2:
            errors['password']="password must be more than 8 charectes"
        return errors


class FilmManeger(models.Manager):
    def basic_validator(self,post_data):
        errors={}
        print (post_data)
        if len(post_data['name'])<3:
             errors['network']="Network must be more than 3 charectes"
           #errors['name']="filmname must be more than 8 charectes"
        if len(post_data['network'])<3:
            errors['network']="Network must be more than 3 charectes"
            
        
            
        if len(post_data['description'])<3:
            errors['description']="description must be more than 3 charectes"
        return errors


class Userr(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.TextField(max_length=20)
    objects=UserrManeger()
  

class Film(models.Model):
    filmname= models.CharField(max_length=20 )
    filmdiscription=models.CharField(max_length=200)
    filmnetwork=models.CharField(max_length=20)
    filmdate= models.DateField()
    filmadder=models.ForeignKey(Userr, related_name="film", on_delete=models.CASCADE)
    objects=FilmManeger()