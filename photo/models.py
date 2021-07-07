from django.db import models


class picture(models.Model):
    img = models.ImageField(blank=True, upload_to="media")
