from django.urls import path
from .views import RegisterProducerView, ProducersListView, ProducerDetailView


urlpatterns = [
    path('register_producer/', RegisterProducerView.as_view(), name="register_producer"),
    path('producers/', ProducersListView.as_view(), name="producer_list"),
    path('producers/<producer_id>/', ProducerDetailView.as_view(), name="producer_detail"),
]
