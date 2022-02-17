from django.db import models


class HeroCard(models.Model):
    title = models.CharField(max_length=150, default="Welcome to PeerToPeer learning")
    overview = models.CharField(max_length=150, default="Delivering Experiences That Students Love")
    image = models.ImageField(upload_to='app-layout/hero-card-wallpapers/',
                              default='app-layout/hero-card-wallpaper/default.jpg')

    def __str__(self):
        return self.title


class HomeworkCard(models.Model):
    alt = models.CharField(max_length=100, default="Simple alt")
    image = models.ImageField(upload_to='app-layout/homework-card-wallpapers/',
                              default='app-layout/homework-card-wallpapers/default.jpg')

    def __str__(self):
        return self.alt


class ScheduleCard(models.Model):
    alt = models.CharField(max_length=100, default="Simple alt")
    image = models.ImageField(upload_to='app-layout/schedule-card-wallpapers/',
                              default='app-layout/schedule-card-wallpapers/default.jpg')

    def __str__(self):
        return self.alt


class ContentSection(models.Model):
    title = models.CharField(max_length=100, default="Section Title")
    content = models.TextField(default="Section Content")

    def __str__(self):
        return self.title


class ContentWithImagesSection(models.Model):
    image = models.ImageField(upload_to='app-layout/ContentWithImages/',
                              default='app-layout/ContentWithImages/default.jpg')
    title = models.CharField(max_length=100, default="Section title")
    content = models.CharField(max_length=150, default="Section subtitle")

    def __str__(self):
        return self.title


class HomeContent(models.Model):
    config_title = models.CharField(max_length=50, default="Config title")
    section_one_title_content = models.ForeignKey(ContentSection, on_delete=models.CASCADE, related_name='section_one',
                                                  default='')
    section_two_title_content = models.ForeignKey(ContentSection, on_delete=models.CASCADE, related_name='section_two',
                                                  default='')
    section_one_with_images_content = models.ForeignKey(ContentWithImagesSection, on_delete=models.CASCADE,
                                                        related_name='section_images_one', default='')
    section_two_with_images_content = models.ForeignKey(ContentWithImagesSection, on_delete=models.CASCADE,
                                                        related_name='section_images_two', default='')
    section_three_with_images_content = models.ForeignKey(ContentWithImagesSection, on_delete=models.CASCADE,
                                                          related_name='section_images_three', default='')

    def __str__(self):
        return self.config_title
