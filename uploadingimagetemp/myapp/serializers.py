from rest_framework import serializers
from .models import Image
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'original_image', 'compressed_image')
        read_only_fields = ["id", 'compressed_image']

    def create(self, validated_data):
        image = validated_data.pop('original_image')
        image_io = BytesIO()
        img = PilImage.open(image)
        img.save(image_io, format='JPEG', quality=30)
        compressed_image_content = ContentFile(image_io.getvalue(), name=image.name)

        instance = Image.objects.create(compressed_image=compressed_image_content, **validated_data)
        return instance
