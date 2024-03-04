from django.urls import path
from . import views

urlpatterns = [
    path('validate_uk_postcode/', views.validate_uk_postcode, name='validate_uk_postcode'),
    path('format_uk_postcode/', views.format_uk_postcode, name='format_uk_postcode'),
    # Add other URL patterns as needed
]