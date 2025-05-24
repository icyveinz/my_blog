from django.db import models

class SquareCard(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='square_cards/')
    background_color = models.CharField(max_length=7, help_text="Hex color code, e.g. #FF5733")

    def __str__(self):
        return self.title
