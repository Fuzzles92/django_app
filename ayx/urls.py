from django.urls import path
from .views import index, decom_request, get_workflows

urlpatterns = [
    path('', index, name='index'),
    path('decom_request/', decom_request, name='decom_request'),
    path('get_workflows/<int:collection_id>/', get_workflows, name='get_workflows'),
]
