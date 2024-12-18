from django.urls import path

from country.views import CountriesAPIView

urlpatterns = [
    path('countries/', CountriesAPIView.as_view(), name='countries'),
    path('countries/<int:pk>/', CountriesAPIView.as_view(), name='country-detail'),
]   