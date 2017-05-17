from django.shortcuts import render

# Create your views here.


from rest_framework import generics
from hello.models import AboutMe,Knowledge,Contact
from .serializers import AboutMeSerializer,KnowledgeSerialiazer,ContactSerializer

class AboutMeAPIView(generics.ListAPIView):
    # queryset = AboutMe.objects.all()
    serializer_class =  AboutMeSerializer
    def get_queryset(self):
        return AboutMe.objects.all()

class KnowledgeView(generics.ListAPIView):
    # queryset = AboutMe.objects.all()
    serializer_class =  KnowledgeSerialiazer
    def get_queryset(self):
        return Knowledge.objects.all()


class ContactView(generics.ListAPIView):
    # queryset = AboutMe.objects.all()
    serializer_class =  ContactSerializer
    def get_queryset(self):
        return Contact.objects.all()