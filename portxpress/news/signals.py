from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver, Signal

from portxpress.utils.unique_slug_generator import unique_slug_generator
from portxpress.news.models import Traffic, News

@receiver(pre_save, sender=News)
def create_news_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=Traffic)
def create_news_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
