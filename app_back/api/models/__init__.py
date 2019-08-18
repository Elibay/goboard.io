import binascii
import os

from django.db import models
from django.contrib.auth import models as auth_models

from django.utils import timezone


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
    lobby = models.ForeignKey('Lobby', related_name='participants', on_delete=models.CASCADE)
    player = models.ForeignKey('Player', related_name='participations', on_delete=models.CASCADE)
    time_joined = models.DateTimeField('Time joined', default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_current = models.BooleanField(default=True)


class Player(models.Model):
    nickname = models.CharField(
        'nickname',
        max_length=150,
        default='Guest',
    )
    user = models.OneToOneField(
        auth_models.User, related_name='profile',
        null=True, verbose_name="", on_delete=models.CASCADE,
    )
    token = models.CharField("Token", max_length=40, default=binascii.hexlify(os.urandom(20)).decode())
    creation_time = models.DateTimeField("CreationTime", auto_now_add=True)

    class Meta:
        verbose_name = 'player'
        verbose_name_plural = 'players'

    def __str__(self):
        return self.nickname + '#' + str(self.id)
