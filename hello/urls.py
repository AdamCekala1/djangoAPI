from django.conf.urls import url,include
from django.contrib import admin

from .views import (
    AboutMeAPIView,
    KnowledgeView,
    ContactView
)
urlpatterns = [
    url(r'^$',AboutMeAPIView.as_view(), name='list'),
    url(r'knowledge/',KnowledgeView.as_view(), name='list'),
    url(r'contact/',ContactView.as_view(), name='list'),
]