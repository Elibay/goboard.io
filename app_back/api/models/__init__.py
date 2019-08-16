import binascii
import os

from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import gettext_lazy as _
#from .authorization import Player
#from .backend import AuthBackend


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
    is_admin = models.BooleanField(default=False)
    is_current = models.BooleanField(default=True)


class Player(models.Model):
    nickname = models.CharField(
        _('nickname'),
        max_length=150,
        default='Guest',
    )

    class Meta:
        verbose_name = _('player')
        verbose_name_plural = _('players')

    def __str__(self):
        return self.nickname + '#' + str(self.id)


class PlayerToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        Player, related_name='token',
        on_delete=models.CASCADE, verbose_name=_("Player")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
