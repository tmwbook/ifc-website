from django.db import models

class Fraternity(models.Model):
    english_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True)
    letters = models.ImageField(upload_to="letters", blank=True)
    primary_color = models.CharField(max_length=7)
    secondary_color = models.CharField(max_length=7)
    featured_picture = models.ImageField(
        upload_to="featured",
        blank=True)
    motto = models.TextField(blank=True)
    values = models.TextField(blank=True)
    extra_info = models.TextField(blank=True)
    house_pic = models.ImageField(
        upload_to="house",
        blank=True)
    calendar_link = models.URLField(blank=True)

    def __str__(self):
        return self.english_name

    def lower_repr(self):
        """Return a lowercase representation of the english name"""
        return ''.join(x for x in self.__str__().lower() if x != " ")

    class Meta:
        verbose_name_plural = "fraternities"