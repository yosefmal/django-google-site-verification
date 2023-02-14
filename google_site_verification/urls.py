from django.urls import re_path

from .views import google_verification_view

urlpatterns = [
    re_path(r'^$', google_verification_view, name='google_verification_view'),
]
