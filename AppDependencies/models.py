from django.db import models


class HeroCard(models.Model):
    title = models.CharField(max_length=150, default="Welcome to PeerToPeer learning")
    overview = models.CharField(max_length=150, default="Delivering Experiences That Students Love")
    image = models.ImageField(upload_to='app-dependencies/hero-card-wallpapers/',
                              default='app-dependencies/hero-card-wallpaper/default.jpg')

    def __str__(self):
        return self.title

