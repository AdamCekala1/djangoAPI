from rest_framework import serializers
from hello.models import AboutMe, Knowledge, Contact
from django.contrib.auth import get_user_model

User = get_user_model()

class KnowledgeSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Knowledge
        fields=[
            'technology',
            'description',
            'icon',
            'id',

        ]

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = [
            'name',
            'surname',
            'description',
            'street',
            'city',
            'phone',
            'email',
            'id'
        ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'imie',
            'nazwisko',
            'miasto',
            'telefon',
            'email',
            'github',
            'facebook',
        ]