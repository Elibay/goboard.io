from django.contrib import admin

from api import models
#from api.models import authorization

# Register your models here.

admin.site.register(models.Player)
admin.site.register(models.Participation)
admin.site.register(models.Lobby)
admin.site.register(models.Game)
