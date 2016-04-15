from django.db import models


class Answer(models.Model):
    text = models.CharField()
    is_valid = models.BooleanField()

    def __str__(self):
        return self.text


class Location(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    logo = models.ImageField()
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    text = models.CharField(max_length=400)
    is_valid = models.BooleanField()

    def __str__(self):
        return self.text


class Question(models.Model):
    exp = models.IntegerField()
    content = models.CharField(max_length=400)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.content


class Quest(models.Model):
    questions = models.ManyToManyField(Question)
    name = models.CharField(max_length=40)
    desc = models.TextField()
    image = models.ImageField()
    bonus = models.IntegerField()
    location = models.OneToOneField(Location)

    def __str__(self):
        return self.name


class Gm(models.Model):
    name = models.CharField(max_length=30, default='')
    nick = models.CharField(max_length=30, default='')
    locations = models.ManyToManyField(Location)
    quests = models.ManyToManyField(Quest)

    def __str__(self):
        return self.name

# Create your models here.
