from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Planets(models.Model):
  box1 = models.CharField(max_length=100)
  box2 = models.CharField(max_length=100)
  box3 = models.CharField(max_length=100)  
  box4 = models.CharField(max_length=100)
  box5 = models.CharField(max_length=100)
  box6 = models.CharField(max_length=100) 
  box7 = models.CharField(max_length=100)
  box8 = models.CharField(max_length=100)
  box9 = models.CharField(max_length=100)
  box10 = models.CharField(max_length=100)
  box11 = models.CharField(max_length=100)
  box12 = models.CharField(max_length=100)  