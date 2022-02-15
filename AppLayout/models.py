from django.db import models


class HeroCard(models.Model):
    title = models.CharField(max_length=150, default="Welcome to PeerToPeer learning")
    overview = models.CharField(max_length=150, default="Delivering Experiences That Students Love")
    image = models.ImageField(upload_to='app-dependencies/hero-card-wallpapers/',
                              default='app-dependencies/hero-card-wallpaper/default.jpg')

    def __str__(self):
        return self.title


class HomeworkCard(models.Model):
    alt = models.CharField(max_length=100, default="Simple alt")
    image = models.ImageField(upload_to='app-dependencies/homework-card-wallpapers/',
                              default='app-dependencies/homework-card-wallpapers/default.jpg')

    def __str__(self):
        return self.alt


class ScheduleCard(models.Model):
    alt = models.CharField(max_length=100, default="Simple alt")
    image = models.ImageField(upload_to='app-dependencies/schedule-card-wallpapers/',
                              default='app-dependencies/schedule-card-wallpapers/default.jpg')

    def __str__(self):
        return self.alt
