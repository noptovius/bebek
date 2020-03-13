from rest_framework import serializers
from Bebek.models import Assistant, AssistantMapping, Transaction, KeyIndicator, Indicator, Review, \
    Semester, Swap
from django.contrib.auth.models import User

class AssistantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assistant

class AssistantMappingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssistantMapping

class SwapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Swap

class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction

class KeyIndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KeyIndicator

class IndicatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicator

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review