from django.contrib import admin
from .models import SquareCard

@admin.register(SquareCard)
class SquareCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'background_color')
