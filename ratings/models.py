from  django.contrib.contenttypes.models import ContentType
from  django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class RatingChoices(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    __empty__ = 'Unknown'

#Rating.objects.aggregate(average=Avg("value"))

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(null=True, blank=True, choices=RatingChoices.choices)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")




