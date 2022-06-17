from django.db import models

# Create your models here.
class Thumbnail(models.Model):
    name = models.CharField("thumbnail name", max_length=60)
    height = models.IntegerField("thumbnail height")

    def __str__(self) -> str:
        return self.name

class Tier(models.Model):
    name = models.CharField("tier name", max_length=30, unique=True)
    original_link_visible = models.BooleanField("original link visibility", default=False)
    expireable = models.BooleanField("expireable", default=False)
    thumbnails = models.ManyToManyField(Thumbnail, related_name="tiers")