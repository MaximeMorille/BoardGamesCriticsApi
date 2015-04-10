from django.db import models

# Create your models here.


class BoardGame(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey('auth.User',
                              related_name='games',
                              null=True,
                              blank=True)
    editor = models.ForeignKey('editors.Editor',
                               related_name='games',
                               null=True,
                               blank=True)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return '%s' % self.name
