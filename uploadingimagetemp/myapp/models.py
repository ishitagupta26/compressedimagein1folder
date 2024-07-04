
from django.db import models
from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile


class Image(models.Model):
    original_image = models.ImageField(upload_to='original_images/', null=True, blank=True)
    compressed_image = models.ImageField(upload_to='compressed_images/')

    def save(self, *args, **kwargs):
        if self.original_image and not self.id:  # Check if new instance and original_image is set
            self.compress_image()
            # Clear original_image to prevent saving it
            self.original_image = None

        super().save(*args, **kwargs)

    def compress_image(self):
        image_io = BytesIO()
        img = PilImage.open(self.original_image)
        img.save(image_io, format='JPEG', quality=30)
        self.compressed_image.save(
            f'compressed_{self.original_image.name}',
            ContentFile(image_io.getvalue()),
            save=False  # Prevent saving temporarily to avoid recursion
        )

    def __str__(self):
        return self.compressed_image.name
