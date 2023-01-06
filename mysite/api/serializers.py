from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Board, Pin


class PinSerializer(serializers.ModelSerializer):

    pin_no  = serializers.IntegerField(required=False)

    class Meta:
        model    = Pin
        fields   = ['name', 'board', 'pin_no', 'status']
        ordering = 'pin_no'


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Board
        fields  = ['id', 'name', 'pin_status']


