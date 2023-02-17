from django.contrib import admin
from django.urls import path, include
import emotion_detect.views as views
from emotion_detect.forms import EmotionForm


urlpatterns = [
    path('', views.emotions, name="emotions"),
 ]