from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from portxpress.utils.unique_slug_generator import unique_slug_generator
from portxpress.request.models import Request

@receiver(pre_save, sender=Request)
def create_news_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

