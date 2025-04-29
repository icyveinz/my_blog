from django.db import models

class UniqueOffer(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.title