from django.urls import path
from .views import get, create

urlpatterns = [
    path('v1/create/', create.CreateStage.as_view(), name='create_stage'),
    path('v1/get/', get.GetAllStages.as_view(), name='get_all_stages'),
    path('v1/get/<uuid:id>/', get.RetriveStage.as_view(), name='retrive_stage'),
]