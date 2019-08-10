from django.contrib import admin
from api import models

# Register your models here.

admin.site.register(models.Player)
admin.site.register(models.Lobby)
admin.site.register(models.Game)
