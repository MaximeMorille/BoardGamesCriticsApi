from django.db import models

# Create your models here.


class Editor(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User',
                              related_name='editors',
                              null=True,
                              blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return '%s' % self.name
