from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    url = models.CharField(max_length=1024, blank=False, null=False)


class Lobby(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    GAME_STATES = (
        ('WAITING', 0),
        ('RUNNING', 1),
        ('FINISHED', 2),
    )
    state = models.IntegerField(choices=GAME_STATES, default=0)


class Participation(models.Model):
    lobby = models.ForeignKey('Lobby', related_name='participants', on_delete=models.DO_NOTHING)
    player = models.ForeignKey('Player', related_name='participations', on_delete=models.DO_NOTHING)
    is_admin = models.BooleanField(default=False)
    is_current = models.BooleanField(default=True)


class Player(auth_models.AbstractBaseUser):
    USERNAME_FIELD = 'name'
    name = models.CharField(max_length=256, default='Guest')
    password = None