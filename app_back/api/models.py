from django.db import models

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    url = models.CharField(max_length=1024, blank=False, null=False)


class Lobby(models.Model):
    url = models.CharField(max_length=1024, blank=False, null=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    GAME_STATES = (
        ('WAITING', 0),
        ('RUNNING', 1),
        ('FINISHED', 2),
    )
    state = models.IntegerField(choices=GAME_STATES, default='WAITING')


class Player(models.Model):
    token = models.CharField(max_length=256, default='shoikh123', blank=False, null=False)
    name = models.CharField(max_length=256, default='Shaik', blank=False, null=False)
    lobby = models.ForeignKey(Lobby, related_name='players', on_delete=models.DO_NOTHING)
    is_admin = models.BooleanField(default=False)
