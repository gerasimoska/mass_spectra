from django.urls import path

from . import views

app_name = "batch"

urlpatterns = [
    path("", views.search_spectra, name="upload"),
    path("download", views.download_csv, name="download"),
]
