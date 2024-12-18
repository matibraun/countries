from celery import shared_task
from .views import CountriesAPIView

@shared_task
def fetch_and_save_countries():

    view = CountriesAPIView()
    view.post(request=None)
    return "Countries fetched and saved successfully."
