from django.db import models


class Domain(models.Model):
    domain = models.CharField(max_length=150, unique=True, default="None")

    def __str__(self):
        return self.domain


class HighSchoolProfile(models.Model):
    profile = models.CharField(max_length=150, unique=True, default="None")

    def __str__(self):
        return self.profile


class Town(models.Model):
    name = models.CharField(max_length=200, unique=True, default="None")

    def __str__(self):
        return self.name


class Universitie(models.Model):
    name = models.CharField(max_length=150, unique=True, default="None")
    town = models.ForeignKey(Town, on_delete=models.CASCADE, default=None, blank=False)

    def __str__(self):
        return self.name


class Facultie(models.Model):
    university = models.ForeignKey(Universitie, on_delete=models.CASCADE, default=None, blank=False)
    name = models.CharField(max_length=150, unique=True, default="None")

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=150, unique=True, default="None")

    def __str__(self):
        return self.name
