from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import utc
from imagekit import ImageSpec, register
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.utils import get_field_info
from accounts.models import CustomUser
import datetime

# Create your models here.

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Image(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    image_url = models.ImageField(upload_to = upload_to, blank = True, null = True)

class ImageThumbnail(ImageSpec):
    options = {'quality': 70}
    @property
    def format(self):
        model, field_name = get_field_info(self.source)
        return model.thumbnail_format
    @property
    def processors(self):
        model, field_name = get_field_info(self.source)
        return [ResizeToFill(model.thumbnail_width, model.thumbnail_height)]

register.generator('imagesapp:thumbnail', ImageThumbnail)

class Thumbnail(models.Model):
    original_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='thumbnails')
    original_source = models.ImageField(upload_to = upload_to, blank = True, null = True)
    thumbnail_url = ImageSpecField(source='original_source', id='imagesapp:thumbnail')
    thumbnail_width = models.PositiveIntegerField()
    thumbnail_height = models.PositiveIntegerField()
    thumbnail_format = models.CharField(max_length=4)

class TemporaryURL(models.Model):
    original_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='temps')
    create_date = models.DateTimeField(auto_now_add=True)
    expire_after = models.PositiveIntegerField(validators=[MaxValueValidator(30000), MinValueValidator(300)])

    def is_expired(self):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        timediff = now - self.create_date
        print(timediff)
        return timediff.total_seconds() < self.expire_after