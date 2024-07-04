from PIL import Image as PilImage
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Image


def compress_image(image):
    image_io = BytesIO()
    img = PilImage.open(image)
    img.save(image_io, format='JPEG', quality=70)
    image_content = ContentFile(image_io.getvalue(), name=image.name)
    return image_content


@receiver(post_save, sender=Image)
def compress_image_signal(sender, instance, created, **kwargs):
    if created:  # Only compress on creation, not on update
        if instance.original_image and not instance.compressed_image:
            instance.compress_image()  # Compresses the original image
            instance.original_image.delete(save=False)  # Deletes the original image file
            instance.original_image = None  # Clears the reference to the original image
            instance.save(update_fields=['compressed_image'])  # Saves the instance with only `compressed_image`
