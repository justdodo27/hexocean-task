from rest_framework import serializers
from .models import Image, Thumbnail
from tiersapp.models import Tier

class ThumbnailSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.ImageField(read_only=True)

    class Meta:
        model = Thumbnail
        fields = ['thumbnail_url']

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'owner']

class ImageCreateSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=True)

    class Meta:
        model = Image
        fields = ['id', 'owner', 'image_url']

    def create(self, validated_data):
        tier = Tier.objects.get(id=validated_data['owner'].tier.id)
        image_format = validated_data['image_url'].content_type.split('/')[-1]
        image = validated_data['image_url'].image

        image_object = Image(owner=validated_data['owner'],image_url = validated_data['image_url'])
        image_object.save()

        for thumbnail_type in tier.thumbnails.all():
            scale_factor = image.size[1] / thumbnail_type.height

            thumbnail = Thumbnail(
                original_image=image_object,
                original_source=validated_data['image_url'],
                thumbnail_width=int(image.size[0] / scale_factor),
                thumbnail_height=thumbnail_type.height,
                thumbnail_format=image_format
            )
            thumbnail.save()
        return image_object

class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(read_only=True)
    thumbnails = ThumbnailSerializer(many=True, read_only=True)

    class Meta:
        model = Image
        fields = ['image_url', 'thumbnails']