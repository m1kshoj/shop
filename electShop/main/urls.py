from django.urls import path, re_path

from .views import *

#
urlpatterns = [
    path('', index, name='home'),  # home - для "динамического" редиректа (хардкод осуждаю)
    path('article/<int:article>', articles)
]
