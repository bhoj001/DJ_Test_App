from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
#from django.contrib.auth.models import User


class Review(models.Model):
    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #object_id = models.PositiveIntegerField()
    #content_object = GenericForeignKey('content_type', 'object_id')
    #user = models.ForeignKey(User)
    post = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    published = models.BooleanField(default=False)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
