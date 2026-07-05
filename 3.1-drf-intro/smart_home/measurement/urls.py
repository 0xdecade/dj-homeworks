from django.urls import path
from .views import SensorsView, SensorDetailView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsView.as_view(), name='sensors-list'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateView.as_view(),
         name='measurement-create'),
]
