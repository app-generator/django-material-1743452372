# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Cliente(models.Model):

    #__Cliente_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField()
    data_cadastro = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Parametro(models.Model):

    #__Parametro_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    valor = models.TextField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField()
    data_cadastro = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Parametro_FIELDS__END

    class Meta:
        verbose_name        = _("Parametro")
        verbose_name_plural = _("Parametro")


class Recurso(models.Model):

    #__Recurso_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    ativo = models.BooleanField()
    data_cadastro = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Recurso_FIELDS__END

    class Meta:
        verbose_name        = _("Recurso")
        verbose_name_plural = _("Recurso")


class Ambiente(models.Model):

    #__Ambiente_FIELDS__
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)
    url = models.TextField(max_length=255, null=True, blank=True)
    database = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    data_cadastro = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Ambiente_FIELDS__END

    class Meta:
        verbose_name        = _("Ambiente")
        verbose_name_plural = _("Ambiente")



#__MODELS__END
